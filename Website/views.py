from django.shortcuts import redirect, render
from django.views.generic import View
from Authentication import models
from django.contrib.auth.forms import UserCreationForm
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
    
class Connection(View):      
    template_name  = "pages/connection.html"
    
    connectForm = UserCreationForm
    
    def get(self, request):       
        return render(request, self.template_name, locals()) 
    
class Register(View):      
    template_name  = "pages/register.html"
    
    def get(self, request):   
        registerForm = NewUserForm    
        return render(request, self.template_name, locals()) 
    
    def post(self, request):  
        template_name  = "pages/register.html"   
        msg =''
        success = True
        if request.method == "POST": 
            registerForm = NewUserForm(request.POST) 
            if registerForm.is_valid():    
                user = registerForm.save()
              
                return redirect("/")
            else:
                registerForm = NewUserForm() 
        return render (request, self.template_name, locals())
                 
        
      
    



# Create your views here.
