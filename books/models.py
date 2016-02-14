# -- coding: utf-8 --
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Book(models.Model):
    name = models.CharField("Nome", max_length=100)
    author = models.CharField("Autor(a)", max_length=200)
    year = models.PositiveSmallIntegerField(
        "Ano", validators=[MinValueValidator(1564), MaxValueValidator(2015)]
    )
    publisher = models.CharField("Editora", max_length=100)

    def __str__(self):
        return '{} - {}'.format(self.author,
                                self.name)
    
    class Meta:
        verbose_name = u"Livro"
        verbose_name_plural = u"Livros"


class BookItem(models.Model):
    book = models.ForeignKey(Book, verbose_name="Livro")

    def __str__(self):
        return '№{} {}'.format(self.pk, self.book.name)
