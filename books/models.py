# -- coding: utf-8 --
from datetime import date
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Book(models.Model):
    name = models.CharField("Nome", max_length=100)
    author = models.CharField("Autor(a)", max_length=200)
    year = models.PositiveSmallIntegerField(
        "Ano", validators=[MinValueValidator(1564), MaxValueValidator(date.today().year)]
    )
    publisher = models.CharField("Editora", max_length=100)

    def __unicode__(self):
        return u'{} - {}'.format(self.author,
                                self.name)
    
    class Meta:
        verbose_name = u"Livro"
        verbose_name_plural = u"Livros"


class BookItem(models.Model):
    book = models.ForeignKey(Book, verbose_name="Livro")

    def __unicode__(self):
        return u'№{} {}'.format(self.pk, self.book.name)
    
    class Meta:
        verbose_name = u"Exemplar"
        verbose_name_plural = u"Exemplares"
