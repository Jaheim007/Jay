from django.db import models
from Features.models import Products
from phonenumber_field.modelfields import PhoneNumberField

class Web_Informations(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    phone = PhoneNumberField()
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()
    linkedIn = models.URLField()
    location_address = models.CharField(max_length=255)
    map_location = models.URLField()
    copyright = models.TextField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    
class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    
class Brands(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    
class Services(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=255)
    delievry_name = models.CharField(max_length=255)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    
class Banner(models.Model):
    main_title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

class Featured_Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    products = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='featured_product')
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    


     
