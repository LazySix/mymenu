# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Place'
        db.create_table(u'restaurant_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('info', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'restaurant', ['Place'])

        # Adding model 'Table'
        db.create_table(u'restaurant_table', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('place', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurant.Place'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('isFree', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'restaurant', ['Table'])

        # Adding model 'ProductCategory'
        db.create_table(u'restaurant_productcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'restaurant', ['ProductCategory'])

        # Adding model 'Product'
        db.create_table(u'restaurant_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurant.ProductCategory'])),
        ))
        db.send_create_signal(u'restaurant', ['Product'])

        # Adding model 'Menu'
        db.create_table(u'restaurant_menu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'restaurant', ['Menu'])

        # Adding M2M table for field products on 'Menu'
        m2m_table_name = db.shorten_name(u'restaurant_menu_products')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('menu', models.ForeignKey(orm[u'restaurant.menu'], null=False)),
            ('product', models.ForeignKey(orm[u'restaurant.product'], null=False))
        ))
        db.create_unique(m2m_table_name, ['menu_id', 'product_id'])

        # Adding model 'Order'
        db.create_table(u'restaurant_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('table', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurant.Table'])),
            ('total', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal(u'restaurant', ['Order'])

        # Adding M2M table for field products on 'Order'
        m2m_table_name = db.shorten_name(u'restaurant_order_products')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('order', models.ForeignKey(orm[u'restaurant.order'], null=False)),
            ('product', models.ForeignKey(orm[u'restaurant.product'], null=False))
        ))
        db.create_unique(m2m_table_name, ['order_id', 'product_id'])


    def backwards(self, orm):
        # Deleting model 'Place'
        db.delete_table(u'restaurant_place')

        # Deleting model 'Table'
        db.delete_table(u'restaurant_table')

        # Deleting model 'ProductCategory'
        db.delete_table(u'restaurant_productcategory')

        # Deleting model 'Product'
        db.delete_table(u'restaurant_product')

        # Deleting model 'Menu'
        db.delete_table(u'restaurant_menu')

        # Removing M2M table for field products on 'Menu'
        db.delete_table(db.shorten_name(u'restaurant_menu_products'))

        # Deleting model 'Order'
        db.delete_table(u'restaurant_order')

        # Removing M2M table for field products on 'Order'
        db.delete_table(db.shorten_name(u'restaurant_order_products'))


    models = {
        u'restaurant.menu': {
            'Meta': {'object_name': 'Menu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['restaurant.Product']", 'symmetrical': 'False'})
        },
        u'restaurant.order': {
            'Meta': {'object_name': 'Order'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['restaurant.Product']", 'symmetrical': 'False'}),
            'table': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restaurant.Table']"}),
            'total': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        u'restaurant.place': {
            'Meta': {'object_name': 'Place'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'restaurant.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restaurant.ProductCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        u'restaurant.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'restaurant.table': {
            'Meta': {'object_name': 'Table'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isFree': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restaurant.Place']"})
        }
    }

    complete_apps = ['restaurant']