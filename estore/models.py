from django.db import models
from users.models import User


class Category(models.Model):
    CATEGORY_NAME = {
        ('Outerwear', 'Outerwear'),
        ('Dresses & Skirts', 'Dresses & Skirts'),
        ('bottoms', 'bottoms'),
        ('Shoes', 'Shoes'),
        ('Accessories', 'Accessories')
    }
    name = models.CharField(max_length=20, choices=CATEGORY_NAME)


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField(max_length=100)
    image = models.ImageField(blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=3)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} |{self.image} | {self.description} | {self.category} | {self.price}"


class Order(models.Model):
    time = models.DateField(auto_now_add=True)
    quantity = models.ImageField()
    total_amount = models.DecimalField(max_digits=100, decimal_places=3,default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)

