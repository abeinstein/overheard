# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Post.has_picture'
        db.add_column(u'posts_post', 'has_picture',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Post.picture_url'
        db.add_column(u'posts_post', 'picture_url',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Post.has_picture'
        db.delete_column(u'posts_post', 'has_picture')

        # Deleting field 'Post.picture_url'
        db.delete_column(u'posts_post', 'picture_url')


    models = {
        u'posts.post': {
            'Meta': {'object_name': 'Post'},
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'facebook_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'has_picture': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'num_comments': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_likes': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'picture_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'poster': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'poster_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'raw_data': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['posts']