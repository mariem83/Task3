from .models import Product, Category
from rest_framework import serializers


class ProdSer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
