#!/usr/bin/env python

from django.contrib.auth.models import User
if User.objects.count() == 0:
    admin = User.objects.create_user('admin', 'admin@folio24.com', 'pass')
    admin.is_superuser = True
    admin.is_staff = True
    admin.save()
