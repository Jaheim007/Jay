from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):    
    email = forms.EmailField(required=True)
    
    class Meta:   
        model = User
        fields = [ 'username', 'email', 'password1', 'password2']
        
        # def username_clean(self):
        #     username = self.cleaned_data['username']
        #     new = User.objects.filter(username = username)
        #     if new.count():
        #         raise forms.ValidationError('Username already exists')
        #     else:
        #         return username
            
        # def email_clean(self):
        #     email = self.email_cleaned_data['email']
        #     new = User.objects.filter(email = email)
        #     if new.count():
        #         raise forms.ValidationError('Email already exists')
        #     else:
        #         return email
            
        # def clean_password2(self):
        #     password1 = self.password1_cleaned_data['password1']
        #     password2 = self.password2_cleaned_data['password2']
        #     if password1 and password2 and password1 != password2:
        #         raise forms.ValidationError("Passwords do not match")
        #     else:
        #         return password2
            
        # def save(self, commit = True): 
        #     user = super(NewUserForm, self).save(commit=False)
        #     user.email = self.cleaned_data['email']
        #     if commit:
        #         user.save()
        #     return user 

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)