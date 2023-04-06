from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .forms import CreateProfile, UpdateProfile
# Create your views here.


# register page
# register page
def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    
    form = CreateProfile()
    if request.method == 'POST':
        forms = CreateProfile(request.POST, request.FILES)

        if forms.is_valid():
            username = forms.cleaned_data.get('username')
            email = forms.cleaned_data.get('email')
            password = forms.cleaned_data.get('password1')
            password2 = forms.cleaned_data.get('password2')
            

            if User.objects.filter(username = username).exists():
                messages.warning(request, 'Username already exist.')
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.warning(request, 'Email already exist.')
                return redirect('register')
            if password != password2:
                messages.warning(request, 'Password not match.')
                return redirect('register')
            
            user = User.objects.create_user(username,email,password)
            forms= forms.save(commit=False)
            forms.user = user
            forms.save()
            messages.success(request, 'Registration successful.')
            
            if "next" in request.GET:
                next_url  = request.GET.get('next')
                return redirect(next_url)

            return redirect('login')
    context={
        'form':form
    }

    return render(request, 'users/register.html',context)

# login page
# login page
def loginuser(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method =='POST':
        username = request.POST.get('uname')
        password = request.POST.get('pwd')

        user = authenticate(username = username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request, 'Login successful.')

            if "next" in request.GET:
                next_url  = request.GET.get('next')
                return redirect(next_url)
            
            return redirect('dashboard')
        else:
            messages.success(request, 'Invalid username/password')
            return redirect('login')
     
    return render(request, 'users/login.html')

# logout page
# logout page
def logoutuser(request):
    logout(request)
    return redirect('login')

    
# dashboard page
# dashboard page
@login_required(login_url=('login'))
def dashboard(request):
    user = request.user.profile
    context={
        'profile':user
    }
    return render(request,'users/dashboard.html',context)


# update page
# update page
@login_required(login_url=('login'))
def update_profile(request):
    user = request.user.profile
    form = UpdateProfile(instance=user)

    if request.method == 'POST':
        forms = UpdateProfile(request.POST, request.FILES, instance=user)
        if forms.is_valid():
            forms.save()
            return redirect('dashboard')

    context={
        'form':form
    }
    return render(request, 'users/update.html', context)

