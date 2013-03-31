# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('accounts_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('photo_count', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('contact_type', self.gf('django.db.models.fields.CharField')(default='M', max_length=1)),
            ('allow_about', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('enable_banner', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('show_get_started', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('page_width', self.gf('django.db.models.fields.PositiveIntegerField')(default=940)),
            ('title_size', self.gf('django.db.models.fields.PositiveIntegerField')(default=50)),
            ('thumbnail_dimension', self.gf('django.db.models.fields.PositiveIntegerField')(default=250)),
            ('font_size', self.gf('django.db.models.fields.FloatField')(default=1.2)),
            ('font_type', self.gf('django.db.models.fields.CharField')(default='S', max_length=1)),
            ('ga_1', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('ga_2', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('copy_text', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('fullname', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('about', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('background_color', self.gf('django.db.models.fields.CharField')(default='000000', max_length=6)),
            ('text_color', self.gf('django.db.models.fields.CharField')(default='999999', max_length=6)),
            ('text_color_hover', self.gf('django.db.models.fields.CharField')(default='D4D4D4', max_length=6)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=500, blank=True)),
            ('blog', self.gf('django.db.models.fields.URLField')(max_length=500, blank=True)),
            ('blog_name', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('blogger', self.gf('django.db.models.fields.URLField')(max_length=500, blank=True)),
            ('deviantart', self.gf('django.db.models.fields.URLField')(max_length=500, blank=True)),
            ('digg', self.gf('django.db.models.fields.URLField')(max_length=500, blank=True)),
            ('facebook', self.gf('django.db.models.fields.URLField')(max_length=500, blank=True)),
            ('flickr', self.gf('django.db.models.fields.URLField')(max_length=500, blank=True)),
            ('google_plus', self.gf('django.db.models.fields.URLField')(max_length=500, blank=True)),
            ('linkedin', self.gf('django.db.models.fields.URLField')(max_length=500, blank=True)),
            ('myspace', self.gf('django.db.models.fields.URLField')(max_length=500, blank=True)),
            ('orkut', self.gf('django.db.models.fields.URLField')(max_length=500, blank=True)),
            ('pinterest', self.gf('django.db.models.fields.URLField')(max_length=500, blank=True)),
            ('tumblr', self.gf('django.db.models.fields.URLField')(max_length=500, blank=True)),
            ('twitter', self.gf('django.db.models.fields.URLField')(max_length=500, blank=True)),
            ('wordpress', self.gf('django.db.models.fields.URLField')(max_length=500, blank=True)),
            ('youtube', self.gf('django.db.models.fields.URLField')(max_length=500, blank=True)),
            ('picture', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('banner', self.gf('imagekit.models.fields.ProcessedImageField')(max_length=100, null=True, blank=True)),
            ('edit_mode', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('accounts', ['UserProfile'])

        # Adding model 'Domains'
        db.create_table('accounts_domains', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('domain', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('accounts', ['Domains'])

        # Adding model 'Customer'
        db.create_table('accounts_customer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stripe_customer_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('account_limit', self.gf('django.db.models.fields.PositiveIntegerField')(default=35)),
        ))
        db.send_create_signal('accounts', ['Customer'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('accounts_userprofile')

        # Deleting model 'Domains'
        db.delete_table('accounts_domains')

        # Deleting model 'Customer'
        db.delete_table('accounts_customer')


    models = {
        'accounts.customer': {
            'Meta': {'object_name': 'Customer'},
            'account_limit': ('django.db.models.fields.PositiveIntegerField', [], {'default': '35'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'flickr': ('django.db.models.fields.URLField', [], {'max_length': '500', 'blank': 'True'}),
            'font_size': ('django.db.models.fields.FloatField', [], {'default': '1.2'}),
            'font_type': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1'}),
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
            'title_size': ('django.db.models.fields.PositiveIntegerField', [], {'default': '50'}),
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