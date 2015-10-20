# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

from django.contrib.auth.hashers import make_password


def create_admin_user(apps, schema_editor):
     User = apps.get_registered_model('auth', 'User')
     admin = User(
         username='admin',
         email='admin@admin.com',
         password=make_password('password'),
         is_superuser=True,
         is_staff=True
     )
     admin.save()


class Migration(migrations.Migration):

    dependencies = [
        ('jenkins', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_admin_user),
    ]
