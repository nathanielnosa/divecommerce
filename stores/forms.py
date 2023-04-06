from django import forms
from .models import Order

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        # fields = ['']
        exclude = ['cart','amount','order_status','discount','subtotal','payment_complete','ref']

        widgets = {
            'order_by': forms.TextInput(attrs={'class':'form-control'}),
            'shipping_address': forms.Textarea(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'payment_method': forms.Select(attrs={'class':'form-control'}),
        }

    