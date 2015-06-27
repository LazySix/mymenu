from decimal import Decimal
import json
import traceback
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



#################### LIST REST VIEWS ############################
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

class ProductQuantityList(APIView):
    @csrf_exempt
    def get(self, request):
        obj = ProductQuantity.objects.all()
        serializer = ProductQuantitySerializer(obj, many=True)
        return JSONResponse(serializer.data)

class OrderList(APIView):
    @csrf_exempt
    def get(self, request):
        obj = Order.objects.all()
        serializer = OrderSerializer(obj, many=True)
        return JSONResponse(serializer.data)


#################### DETAIL REST VIEWS ############################

class ProductCategoryDetail(APIView):
    @csrf_exempt
    def get(self, request, pk):
        try:
            obj = ProductCategory.objects.get(pk=pk)
        except:
            return HttpResponse(status=404)
        serializer = ProductCategorySerializer(obj)
        return JSONResponse(serializer.data)


class ProductDetail(APIView):
    @csrf_exempt
    def get(self, request, pk):
        try:
            obj = Product.objects.get(pk=pk)
        except:
            return HttpResponse(status=404)
        serializer = ProductSerializer(obj)
        return JSONResponse(serializer.data)

class MenuDetail(APIView):
    @csrf_exempt
    def get(self, request, pk):
        try:
            obj = Menu.objects.get(pk=pk)
        except:
            return HttpResponse(status=404)
        serializer = MenuSerializer(obj)
        return JSONResponse(serializer.data)

class PlaceDetail(APIView):
    @csrf_exempt
    def get(self, request, pk):
        try:
            obj = Place.objects.get(pk=pk)
        except:
            return HttpResponse(status=404)
        serializer = PlaceSerializer(obj)
        return JSONResponse(serializer.data)

class TableDetail(APIView):
    @csrf_exempt
    def get(self, request, pk):
        try:
            obj = Table.objects.get(pk=pk)
        except:
            return HttpResponse(status=404)
        serializer = TableSerializer(obj)
        return JSONResponse(serializer.data)

class ProductQuantityDetail(APIView):
    @csrf_exempt
    def get(self, request, pk):
        try:
            obj = ProductQuantity.objects.get(pk=pk)
        except:
            return HttpResponse(status=404)
        serializer = ProductQuantitySerializer(obj)
        return JSONResponse(serializer.data)

class OrderDetail(APIView):
    @csrf_exempt
    def get(self, request, pk):
        try:
            obj = Order.objects.get(pk=pk)
        except:
            return HttpResponse(status=404)
        serializer = OrderSerializer(obj)
        return JSONResponse(serializer.data)


class PostRequests(APIView):
    @csrf_exempt
    def post(self, request, pk, format=None):
        try:
            jsonres = request.body
            result = json.loads(jsonres)
            table = Table.objects.get(pk=pk)
            if result['action'] == 'sit_on_this_table':
                if not table.isFree:
                    return JSONResponse({'error': True, 'reason': 'Table is not free'})
                else:
                    table.isFree = False
                    table.save()
                    order = Order.objects.create(table=table, isFinished=False)
                    order_id = order.id
                    return JSONResponse({'order_id': order_id})

            if result['action'] == 'add_in_order':
                order = None
                for ord in table.order_set.all():
                    if not ord.isFinished:
                        order = ord
                if not order:
                    return JSONResponse({'error': True, 'reason': "This table doesn't have unfinished orders"})
                else:
                    products = result['products']
                    for product in products:
                        curr_product = Product.objects.get(pk=product)
                        curr_quantity = products[product]
                        pc = ProductQuantity(product=curr_product, quantity=curr_quantity)
                        pc.save()
                        order.products_quantity.add(pc)
                        if order.total:
                            order.total += curr_product.price * curr_quantity
                        else:
                            order.total = Decimal(0.00)
                            order.total += curr_product.price * curr_quantity
                    order.save()
                    return JSONResponse(True)

            if result['action'] == 'pay_the_bill':
                order = None
                for ord in table.order_set.all():
                    if not ord.isFinished:
                        order = ord
                if not order:
                    return JSONResponse({'error': True, 'reason': "This table doesn't have unfinished orders"})
                else:
                    order.isFinished = True
                    table.isFree = True
                    order.save()
                    table.save()
                    return JSONResponse(True)

            return JSONResponse({"status": "Unknown action"})

        except Exception as e:
            print traceback.print_exc()
            return JSONResponse({'error': True, 'reason': 'Server error'})