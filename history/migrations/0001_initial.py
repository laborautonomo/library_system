# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('date_taken', models.DateField(verbose_name='Emprestado em')),
                ('date_due', models.DateField(verbose_name='À ser entregue em')),
                ('date_returned', models.DateField(blank=True, verbose_name='Entregue em', null=True)),
                ('fine', models.SmallIntegerField(verbose_name='Multa total', default=0)),
                ('daily_fine', models.SmallIntegerField(verbose_name='Multa diária', default=0)),
                ('is_fine_paid', models.NullBooleanField(verbose_name='Multa paga?', default=False)),
                ('book_item', models.ForeignKey(to='books.BookItem')),
            ],
        ),
    ]
