# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20170901_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normalpost',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
