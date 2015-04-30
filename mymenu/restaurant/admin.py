from django.contrib import admin
from .models import *


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


class ProductQuantityAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.total = sum(pr_q.product.price * pr_q.quantity for pr_q in form.cleaned_data['products_quantity'])
        obj.save()


admin.site.register(Place, PlaceAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductQuantity, ProductQuantityAdmin)