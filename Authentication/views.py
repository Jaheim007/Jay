from django.shortcuts import render , redirect
from django.views.generic import View
from Authentication import models
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from Authentication import forms

class Connection(View):      
    template_name  = "pages/connection.html"
    
    def get(self , request):
        return render(request, self.template_name, locals()) 
    
    
    def post(self, request):
        # if request.method == "POST":
        #     connectform = AuthenticationForm(request, data =request.POST)
        #     if connectform.is_valid():
        #         username = connectform.cleaned_data.get('username')
        #         password = connectform.cleaned_data.get('password')
        #         if user is not None:
                
        pass        
        
class Register(View):      
    template_name  = "pages/register.html"
    
    def get(self, request):   
        registerForm = forms.NewUserForm   
        return render(request, self.template_name, locals()) 
    
    def post(self, request):  
        if request.method == "POST": 
            registerForm = forms.NewUserForm(request.POST)
            if registerForm.is_valid():  
                registerForm.save()
                print("done")       
            return redirect("/connection")
        return render(request, self.template_name, locals()) 

# Create your views here.
