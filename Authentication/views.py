from django.shortcuts import render , redirect
from django.views.generic import View
from django.contrib import messages
from django.forms import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from Authentication import forms

      
class Register(View):      
    template_name  = "pages/register.html"
    
    def get(self, request):   
        form = forms.NewUserForm   
        return render(request, self.template_name, locals()) 
    
    def post(self, request):  
        if request.method == "POST": 
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")

            user = User(
                username = username, 
                email = email, 
                password = password1,  
            )
            
            user.save()
            login(request, user)
            return redirect("/connection")
        
        return render(request, self.template_name,locals()) 

class Connection(View): 
    form = forms.LoginForm  
    template_name  = "pages/connection.html"
    
    def get(self , request):
        
        return render(request, self.template_name, context={"form": self.form}) 
    
    
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():     
            user = authenticate(
                username=form.cleaned_data["username"], 
                password= form.cleaned_data["password"]
            )
            print(user)
            if user is not None:
                login(request, user)
                return redirect("/") 
            else:     
                print("User not Found") 
                
               
                
            # if form.is_valid():
            #     username = form.cleaned_data.get('username')
            #     password = form.cleaned_data.get('password')
            #     user = authenticate(username=username, password=password)
            #     if user is not None:
            #         print(user)
            #         login(request, user)
            #         return redirect("/")
            #     else:     
            #         print("User not Found")
        return render(request, self.template_name,locals()) 
    
                
