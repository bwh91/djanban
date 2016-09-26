# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djanban', '0002_auto_20160924_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='complete',
        ),
        migrations.AddField(
            model_name='story',
            name='staus',
            field=models.CharField(choices=[('ToDo', 'ToDo'), ('doing', 'Doing'), ('Done', 'DONE')], default='ToDo', max_length=5),
        ),
    ]
