# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserDetail',
        ),
        migrations.RemoveField(
            model_name='user',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='user',
            name='visit',
        ),
    ]
