# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-24 21:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bug',
            old_name='user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='bug',
            old_name='created',
            new_name='created_date',
        ),
    ]