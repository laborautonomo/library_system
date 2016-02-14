# -- coding: utf-8 --
import datetime

from django.db import models

from books.models import BookItem
from readers.models import Reader


class HistoryItem(models.Model):
    date_taken = models.DateField(verbose_name="Data de emissão")
    date_due = models.DateField(verbose_name="Data de vencimento")
    date_returned = models.DateField(verbose_name="Data do retorno", blank=True, null=True)
    fine = models.SmallIntegerField(verbose_name="Multa total", default=0)
    daily_fine = models.SmallIntegerField("Multa diária", default=1)
    is_fine_paid = models.NullBooleanField(verbose_name="Bom pagador(a)?", default=False)
    book_item = models.ForeignKey(BookItem)
    reader = models.ForeignKey(Reader)

    def __str__(self):
        return '{}: №{} {} - {}'.format(
            self.reader.username, self.book_item.pk,
            self.book_item.book.author,
            self.book_item.book.name
        )

    def calculate_fine(self):
        if self.date_due < datetime.date.today():
            if not self.date_returned:
                return self.daily_fine * (datetime.date.today() - self.date_due).days
            elif self.date_returned > self.date_due:
                return self.daily_fine * (self.date_returned - self.date_due).days
            else:
                return 0
        else:
            return 0

    def save(self, *args, **kwargs):
        self.fine = self.calculate_fine()
        super(HistoryItem, self).save(*args, **kwargs)
