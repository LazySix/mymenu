from django.contrib import admin
from .models import *
# Register your models here.


class PlaceAdmin(admin.ModelAdmin):
    pass

class TableAdmin(admin.ModelAdmin):
    pass

class ProductCategoryAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    pass

class MenuAdmin(admin.ModelAdmin):
    pass

class OrderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Place, PlaceAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Order, OrderAdmin)