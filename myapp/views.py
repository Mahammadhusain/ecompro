from django.shortcuts import render

# Create your views here.
def HomeView(request):
    return render(request,'home.html')
def AllProductsView(request):
    return render(request,'allproducts.html')
def CartView(request):
    return render(request,'cart.html')
def CheckoutView(request):
    return render(request,'checkout.html')
def OrdersView(request):
    return render(request,'orders.html')

def ContactView(request):
    return render(request,'contact.html')

def AboutView(request):
    return render(request,'about.html')









# Auth Section ------------------------------
def SigninView(request):
    return render(request,'signin.html')
def SignupView(request):
    return render(request,'signup.html')
def ProfileView(request):
    return render(request,'profile.html')
def AddressView(request):
    return render(request,'address.html')
def PassChangeView(request):
    return render(request,'changepass.html')