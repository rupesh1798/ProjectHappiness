# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20170829_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]