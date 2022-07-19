from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField()
    active = models.BooleanField(default=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    
class Products(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    currency = models.CharField(max_length=20)
    price = models.FloatField()
    stocks = models.IntegerField()
    size = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    description = models.TextField()
    specfication = models.TextField()
    color = models.CharField(max_length=255)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    



