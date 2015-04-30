# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field products_qnatity on 'Order'
        db.delete_table(db.shorten_name(u'restaurant_order_products_qnatity'))

        # Adding M2M table for field products_quantity on 'Order'
        m2m_table_name = db.shorten_name(u'restaurant_order_products_quantity')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('order', models.ForeignKey(orm[u'restaurant.order'], null=False)),
            ('productquantity', models.ForeignKey(orm[u'restaurant.productquantity'], null=False))
        ))
        db.create_unique(m2m_table_name, ['order_id', 'productquantity_id'])


    def backwards(self, orm):
        # Adding M2M table for field products_qnatity on 'Order'
        m2m_table_name = db.shorten_name(u'restaurant_order_products_qnatity')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('order', models.ForeignKey(orm[u'restaurant.order'], null=False)),
            ('productquantity', models.ForeignKey(orm[u'restaurant.productquantity'], null=False))
        ))
        db.create_unique(m2m_table_name, ['order_id', 'productquantity_id'])

        # Removing M2M table for field products_quantity on 'Order'
        db.delete_table(db.shorten_name(u'restaurant_order_products_quantity'))


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
            'isFinished': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'products_quantity': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['restaurant.ProductQuantity']", 'symmetrical': 'False'}),
            'table': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restaurant.Table']"}),
            'total': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'})
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
        u'restaurant.productquantity': {
            'Meta': {'object_name': 'ProductQuantity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['restaurant.Product']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '1'})
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