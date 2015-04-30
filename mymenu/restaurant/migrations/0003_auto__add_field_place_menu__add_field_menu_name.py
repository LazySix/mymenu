# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Place.menu'
        db.add_column(u'restaurant_place', 'menu',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['restaurant.Menu']),
                      keep_default=False)

        # Adding field 'Menu.name'
        db.add_column(u'restaurant_menu', 'name',
                      self.gf('django.db.models.fields.CharField')(default='SomeName', max_length=510),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Place.menu'
        db.delete_column(u'restaurant_place', 'menu_id')

        # Deleting field 'Menu.name'
        db.delete_column(u'restaurant_menu', 'name')


    models = {
        u'restaurant.menu': {
            'Meta': {'object_name': 'Menu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '510'}),
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
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restaurant.Menu']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'restaurant.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restaurant.ProductCategory']"}),
            'full_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '1023', 'null': 'True', 'blank': 'True'})
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