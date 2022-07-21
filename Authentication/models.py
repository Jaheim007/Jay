from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


    
class Newsletter(models.Model):
    email = models.EmailField(max_length=254)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=254)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    

    
    
    
    

# Create your models here.
