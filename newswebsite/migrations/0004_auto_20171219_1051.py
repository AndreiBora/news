# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-12-19 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newswebsite', '0003_comment2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment2',
        ),
        migrations.AddField(
            model_name='comment',
            name='page',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
