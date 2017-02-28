# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-10 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_status', models.CharField(default='\u5f85\u5ba1\u6838', max_length=20)),
                ('publish_type', models.CharField(default='\u589e\u91cf\u90e8\u7f72', max_length=20)),
                ('publish_module', models.CharField(max_length=30)),
                ('publish_filename', models.CharField(max_length=30)),
                ('file_uploadtime', models.CharField(default=b'00-00-00 00:00:00', max_length=30)),
                ('publish_user', models.CharField(max_length=16)),
                ('review_owner', models.CharField(default=b'-', max_length=30)),
                ('create_time', models.CharField(max_length=30)),
                ('publish_serverlist', models.CharField(max_length=256)),
                ('publish_detail', models.TextField(default=b'', max_length=1024)),
                ('is_active', models.CharField(default=b'0', max_length=2)),
                ('update_user', models.CharField(blank=True, max_length=16, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_id', models.CharField(max_length=30)),
                ('publish_status', models.CharField(max_length=30)),
                ('publish_type', models.CharField(default='\u589e\u91cf\u90e8\u7f72', max_length=30)),
                ('publish_module', models.CharField(max_length=30)),
                ('publish_filename', models.CharField(max_length=30)),
                ('file_uploadtime', models.CharField(default=b'00-00-00 00:00:00', max_length=30)),
                ('publish_user', models.CharField(max_length=16)),
                ('create_time', models.CharField(max_length=30)),
                ('publish_serverlist', models.CharField(max_length=256)),
                ('publish_detail', models.TextField(default=b'-', max_length=1024)),
                ('review_owner', models.CharField(max_length=30)),
                ('review_time', models.CharField(max_length=30)),
                ('review_info', models.TextField(max_length=1024)),
                ('publish_strtime', models.CharField(blank=True, default=b'00-00-00 00:00:00', max_length=30, null=True)),
                ('publish_endtime', models.CharField(blank=True, default=b'00-00-00 00:00:00', max_length=30, null=True)),
                ('is_active', models.CharField(default=b'0', max_length=2)),
                ('update_user', models.CharField(blank=True, max_length=16, null=True)),
            ],
        ),
    ]
