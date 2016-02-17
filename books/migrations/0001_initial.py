# -*- coding: utf-8 -*-
from datetime import date

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Nome', max_length=100)),
                ('author', models.CharField(verbose_name='Autor(a)', max_length=200)),
                ('year', models.PositiveSmallIntegerField(verbose_name='Ano', validators=[django.core.validators.MinValueValidator(1564), django.core.validators.MaxValueValidator(date.today().year)])),
                ('publisher', models.CharField(verbose_name='Editora', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BookItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('book', models.ForeignKey(verbose_name='Livro', to='books.Book')),
            ],
        ),
    ]
