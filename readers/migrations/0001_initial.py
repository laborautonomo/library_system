# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.contrib.auth.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, to=settings.AUTH_USER_MODEL, serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(blank=True, verbose_name='Telefone', max_length=16)),
                ('address', models.CharField(blank=True, verbose_name='Endereço', max_length=50)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
