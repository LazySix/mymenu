from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Product Category'
        verbose_name_plural = verbose_name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('ProductCategory')
    short_description = models.CharField(max_length=1023, null=True, blank=True)
    full_description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Product'
        verbose_name_plural = verbose_name


class Menu(models.Model):
    name = models.CharField(max_length=510)
    products = models.ManyToManyField('Product')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Menu'
        verbose_name_plural = verbose_name


class Place(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    info = models.TextField(null=True, blank=True)
    menu = models.ForeignKey('Menu')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Place'
        verbose_name_plural = verbose_name


class Table(models.Model):
    place = models.ForeignKey('Place')
    code = models.CharField(max_length=255, null=True, blank=True)
    isFree = models.BooleanField(default=True)

    def __unicode__(self):
        return self.code

    class Meta:
        verbose_name = u'Table'
        verbose_name_plural = verbose_name


class Order(models.Model):
    table = models.ForeignKey('Table')
    products = models.ManyToManyField('Product')
    isFinished = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __unicode__(self):
        return u'Order for table: %s' % self.table.code

    class Meta:
        verbose_name = u'Order'
        verbose_name_plural = verbose_name