# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'posts_post', (
            ('facebook_id', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
            ('body', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('num_likes', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('num_comments', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('poster', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('poster_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('raw_data', self.gf('jsonfield.fields.JSONField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'posts', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'posts_post')


    models = {
        u'posts.post': {
            'Meta': {'object_name': 'Post'},
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'facebook_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'num_comments': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_likes': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'poster': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'poster_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'raw_data': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['posts']