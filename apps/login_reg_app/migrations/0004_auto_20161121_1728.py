# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg_app', '0003_user_trips'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='trips',
            field=models.ManyToManyField(related_name='users', to='app1.Destination'),
        ),
    ]
