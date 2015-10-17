# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('credential', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='JenkinsJob',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('credential', models.ForeignKey(blank=True, to='jenkins.Credential', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JenkinsJobStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('identifier', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
                ('job', models.ForeignKey(to='jenkins.JenkinsJob')),
            ],
        ),
    ]
