# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 17:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictaroo', '0003_auto_20170307_1945'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Page',
            new_name='Image',
        ),
    ]
