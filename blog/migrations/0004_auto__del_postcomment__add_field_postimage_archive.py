# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PostComment'
        db.delete_table(u'blog_postcomment')

        # Adding field 'PostImage.archive'
        db.add_column(u'blog_postimage', 'archive',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'PostComment'
        db.create_table(u'blog_postcomment', (
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.CharField')(default='anonymous', max_length=255)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='replies', null=True, to=orm['blog.PostComment'], blank=True)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comments', to=orm['blog.Post'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'blog', ['PostComment'])

        # Deleting field 'PostImage.archive'
        db.delete_column(u'blog_postimage', 'archive')


    models = {
        u'blog.post': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Post'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'blog.postimage': {
            'Meta': {'object_name': 'PostImage'},
            'archive': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': u"orm['blog.Post']"})
        }
    }

    complete_apps = ['blog']