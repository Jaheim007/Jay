from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Customers(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    
    GENDER = [
        (MALE, 'male'), 
        (FEMALE, 'female')
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    date_of_birth = models.DateField()
    gender = models.CharField(choices=GENDER, max_length=255)
    phone_number = PhoneNumberField()
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    
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
