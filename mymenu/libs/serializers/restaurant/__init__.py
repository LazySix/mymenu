from rest_framework import serializers
from restaurant.models import *


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order