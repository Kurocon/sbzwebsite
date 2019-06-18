# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-06-18 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hygiene', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkday',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='checkdayitem',
            name='result',
            field=models.CharField(choices=[('GOOD', '✓'), ('ACCEPT', '~'), ('BAD', '✗')], max_length=8),
        ),
    ]
