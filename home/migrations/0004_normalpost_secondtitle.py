# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_normalpost_readmore'),
    ]

    operations = [
        migrations.AddField(
            model_name='normalpost',
            name='SecondTitle',
            field=models.CharField(blank=True, default='readmore', max_length=8, null=True),
        ),
    ]
