from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    price = models.IntegerField()
    length = models.IntegerField()
    width = models.IntegerField()
    weight = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
