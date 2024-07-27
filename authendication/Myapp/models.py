from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100, default='')  # Changed default from 0 to an empty string
    
    def __str__(self):
        return self.email

class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()  # Removed max_length argument as it's not valid for IntegerField
    stock = models.PositiveBigIntegerField()
    price = models.IntegerField()
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name
