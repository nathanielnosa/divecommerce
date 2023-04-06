from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name='index'),
    path('category/<str:id>/',views.category, name='category'),
    path('products',views.products,name='products'),
    path('product/<str:id>/',views.product,name='product'),
    path('search/',views.search,name='search'),
    path('addtocart/<str:id>/', views.add_to_cart, name='addtocart'),
    path('mycart',views.myCart,name='mycart'),
    path('managecart/<str:id>/',views.managecart,name='managecart'),
    path('checkout/',views.checkout, name='checkout'),

    path('payment/<str:id>/', views.payment, name='payment'),
    # path('tpayment/<str:id>/', views.tpayment, name='tpayment'),
    path('<str:ref>/',views.verify_payment,name='verify-payment')

]