from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from libs.serializers.restaurant import *
from restaurant.models import *


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class ProductCategoryList(APIView):
    @csrf_exempt
    def get(self, request):
        obj = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(obj, many=True)
        return JSONResponse(serializer.data)


class ProductList(APIView):
    @csrf_exempt
    def get(self, request):
        obj = Product.objects.all()
        serializer = ProductSerializer(obj, many=True)
        return JSONResponse(serializer.data)

class MenuList(APIView):
    @csrf_exempt
    def get(self, request):
        obj = Menu.objects.all()
        serializer = MenuSerializer(obj, many=True)
        return JSONResponse(serializer.data)

class PlaceList(APIView):
    @csrf_exempt
    def get(self, request):
        obj = Place.objects.all()
        serializer = PlaceSerializer(obj, many=True)
        return JSONResponse(serializer.data)

class TableList(APIView):
    @csrf_exempt
    def get(self, request):
        obj = Table.objects.all()
        serializer = TableSerializer(obj, many=True)
        return JSONResponse(serializer.data)

class OrderList(APIView):
    @csrf_exempt
    def get(self, request):
        obj = Order.objects.all()
        serializer = OrderSerializer(obj, many=True)
        return JSONResponse(serializer.data)