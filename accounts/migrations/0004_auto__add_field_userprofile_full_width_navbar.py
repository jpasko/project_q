# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UserProfile.full_width_navbar'
        db.add_column('accounts_userprofile', 'full_width_navbar',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UserProfile.full_width_navbar'
        db.delete_column('accounts_userprofile', 'full_width_navbar')


    models = {
        'accounts.customer': {
            'Meta': {'object_name': 'Customer'},
            'account_limit': ('django.db.models.fields.PositiveIntegerField', [], {'default': '35'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_file_size': ('django.db.models.fields.PositiveIntegerField', [], {'default': '2'}),
            'stripe_customer_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'accounts.domains': {
            'Meta': {'object_name': 'Domains'},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'accounts.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'allow_about': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'background_color': ('django.db.models.fields.CharField', [], {'default': "'000000'", 'max_length': '6'}),
            'banner': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'blog': ('django.db.models.fields.URLField', [], {'max_length': '500', 'blank': 'True'}),
            'blog_name': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'blogger': ('django.db.models.fields.URLField', [], {'max_length': '500', 'blank': 'True'}),
            'contact_type': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            'copy_text': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'deviantart': ('django.db.models.fields.URLField', [], {'max_length': '500', 'blank': 'True'}),
            'digg': ('django.db.models.fields.URLField', [], {'max_length': '500', 'blank': 'True'}),
            'edit_mode': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'enable_banner': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '500', 'blank': 'True'}),
            'favicon': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'flickr': ('django.db.models.fields.URLField', [], {'max_length': '500', 'blank': 'True'}),
            'font_size': ('django.db.models.fields.FloatField', [], {'default': '1.2'}),
            'font_type': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1'}),
            'full_width_navbar': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fullname': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'ga_1': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ga_2': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'google_plus': ('django.db.models.fields.URLField', [], {'max_length': '500', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkedin': ('django.db.models.fields.URLField', [], {'max_length': '500', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'myspace': ('django.db.models.fields.URLField', [], {'max_length': '500', 'blank': 'True'}),
            'orkut': ('django.db.models.fields.URLField', [], {'max_length': '500', 'blank': 'True'}),
            'page_width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '940'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'photo_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'picture': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'pinterest': ('django.db.models.fields.URLField', [], {'max_length': '500', 'blank': 'True'}),
            'show_get_started': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'text_color': ('django.db.models.fields.CharField', [], {'default': "'999999'", 'max_length': '6'}),
            'text_color_hover': ('django.db.models.fields.CharField', [], {'default': "'D4D4D4'", 'max_length': '6'}),
            'thumbnail_dimension': ('django.db.models.fields.PositiveIntegerField', [], {'default': '250'}),
            'title_size': ('django.db.models.fields.PositiveIntegerField', [], {'default': '30'}),
            'tumblr': ('django.db.models.fields.URLField', [], {'max_length': '500', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '500', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '500', 'blank': 'True'}),
            'wordpress': ('django.db.models.fields.URLField', [], {'max_length': '500', 'blank': 'True'}),
            'youtube': ('django.db.models.fields.URLField', [], {'max_length': '500', 'blank': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['accounts']