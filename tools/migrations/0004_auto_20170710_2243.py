# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0003_certificate_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='password',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
    ]