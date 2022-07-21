from django.shortcuts import redirect, render
from django.views.generic import View
from Authentication import models
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from Authentication.forms import NewUserForm


class Homepage(View):
    template_name = 'pages/index.html'

    def get(self , request):
        return render(request, self.template_name)
    
    def post(self, request):
        pass
    
class Aboutpage(View):
    template_name = "pages/about.html"
    
    
    
    def get(self , request):
        return render(request, self.template_name, )
    
    def post(self , request):
        pass
    
class Contact(View):
    template_name = "pages/contact.html"
    
    def get(self , request):
        return render(request, self.template_name)
    
    def post(self , request):
        pass

class Shopsingle(View):  
    template_name = "pages/shop-single.html"
    
    def get(self , request):
        return render(request, self.template_name)
    
    def post(self , request):
        pass

class Shop(View):
    template_name = "pages/shop.html"
    
    def get(self , request):
        return render(request, self.template_name)
    
    def post(self , request):
        pass
    
        
                 
 
      
    



# Create your views here.
