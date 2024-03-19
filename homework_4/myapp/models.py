from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}, age: {self.age}'
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    price = models.FloatField()
    image = models.ImageField()

    def __str__(self):
        return f'Name: {self.name}, description: {self.description}, price: {self.price}'