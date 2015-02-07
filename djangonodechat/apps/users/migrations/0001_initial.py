# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(unique=True, max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('avatar', models.URLField()),
                ('slug', models.SlugField(null=True, unique=True, blank=True, max_length=250)),
                ('visit', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(verbose_name='groups', related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', blank=True, related_name='user_set', to='auth.Group')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', related_query_name='user', help_text='Specific permissions for this user.', blank=True, related_name='user_set', to='auth.Permission')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('aboutme', models.TextField(default='Acerca de Mi ...', null=True, validators=[django.core.validators.MaxLengthValidator(500)], blank=True)),
                ('location', models.CharField(null=True, max_length=100, blank=True)),
                ('facebook', models.CharField(null=True, max_length=250, blank=True)),
                ('twitter', models.CharField(null=True, max_length=250, blank=True)),
                ('googleplus', models.CharField(null=True, max_length=250, blank=True)),
                ('instagram', models.CharField(null=True, max_length=250, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
