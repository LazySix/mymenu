from django.conf.urls import patterns, include, url

from django.contrib import admin
from libs.subviews.rest import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mymenu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include(admin.site.urls)),
    url(r'^api/rest/product-category/all/$', ProductCategoryList.as_view(), name="All Product categories"),
    url(r'^api/rest/product/all/$', ProductList.as_view(), name="All Products"),
    url(r'^api/rest/menu/all/$', MenuList.as_view(), name="All Menus"),
    url(r'^api/rest/place/all/$', PlaceList.as_view(), name="All Places"),
    url(r'^api/rest/table/all/$', TableList.as_view(), name="All Tables"),
    url(r'^api/rest/order/all/$', OrderList.as_view(), name="All Orders"),
)
