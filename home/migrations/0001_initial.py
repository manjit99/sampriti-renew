# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 13:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NormalPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=500)),
                ('Image', models.FileField(blank=True, null=True, upload_to='')),
                ('Timestamp', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('About', models.TextField()),
            ],
        ),
    ]
