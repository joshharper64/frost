# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 00:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resident_reports', '0002_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='topic',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]