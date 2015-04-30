from django.conf.urls import patterns, include, url

from django.contrib import admin
from libs.subviews.rest import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include(admin.site.urls)),
    url(r'^api/rest/categories/$', ProductCategoryList.as_view(), name="All Product categories"),
    url(r'^api/rest/products/$', ProductList.as_view(), name="All Products"),
    url(r'^api/rest/menus/$', MenuList.as_view(), name="All Menus"),
    url(r'^api/rest/places/$', PlaceList.as_view(), name="All Places"),
    url(r'^api/rest/tables/$', TableList.as_view(), name="All Tables"),
    url(r'^api/rest/orders/$', OrderList.as_view(), name="All Orders"),

    url(r'^api/rest/product-category/(?P<pk>[0-9]+)/$', ProductCategoryDetail.as_view(), name="Product category"),
    url(r'^api/rest/product/(?P<pk>[0-9]+)/$', ProductDetail.as_view(), name="Product"),
    url(r'^api/rest/menu/(?P<pk>[0-9]+)/$', MenuDetail.as_view(), name="Menu"),
    url(r'^api/rest/place/(?P<pk>[0-9]+)/$', PlaceDetail.as_view(), name="Place"),
    url(r'^api/rest/table/(?P<pk>[0-9]+)/$', TableDetail.as_view(), name="Table"),
    url(r'^api/rest/order/(?P<pk>[0-9]+)/$', OrderDetail.as_view(), name="Order"),
)
