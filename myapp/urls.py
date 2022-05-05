from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    
    path('', HomeView,name='home'),
    path('allprod/', AllProductsView,name='allprod'),
    path('cart/', CartView,name='cart'),
    path('orders/', OrdersView,name='orders'),
    path('checkout/', CheckoutView,name='checkout'),
    path('contact/', ContactView,name='contact'),
    path('about/', AboutView,name='about'),


    # Auth ---------------------------------------
    path('signin/', SigninView,name='signin'),
    path('signup/', SignupView,name='signup'),
    path('profile/', ProfileView,name='profile'),
    path('passchange/', PassChangeView,name='passchange'),
    path('address/', AddressView,name='address'),
    
]
