from rest_framework import serializers
from restaurant.models import *


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory

class ProductSerializer(serializers.ModelSerializer):

    category = ProductCategorySerializer(many=False)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'category', 'short_description', 'full_description')

class MenuSerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True)

    class Meta:
        model = Menu
        fields = ('id', 'name', 'products')

class PlaceSerializer(serializers.ModelSerializer):

    menu = MenuSerializer(many=False)

    class Meta:
        model = Place
        fields = ('id', 'name', 'info', 'menu')

class TableSerializer(serializers.ModelSerializer):

    place = PlaceSerializer(many=False)

    class Meta:
        model = Table
        fields = ('id', 'place', 'code', 'isFree')

class OrderSerializer(serializers.ModelSerializer):

    table = TableSerializer(many=False)
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'table', 'products', 'total')