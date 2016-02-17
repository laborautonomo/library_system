# -- coding: utf-8 --
import datetime

from django.db import models

from books.models import BookItem
from readers.models import Reader


class HistoryItem(models.Model):
    date_taken = models.DateField(verbose_name="Emprestado em")
    date_due = models.DateField(verbose_name="À ser entregue em")
    date_returned = models.DateField(verbose_name="Entregue em", blank=True, null=True)
    fine = models.SmallIntegerField(verbose_name="Multa total", default=0)
    daily_fine = models.SmallIntegerField("Multa diária", default=0)
    is_fine_paid = models.NullBooleanField(verbose_name="Multa paga?", default=False)
    book_item = models.ForeignKey(BookItem)
    reader = models.ForeignKey(Reader)

    def __unicode__(self):
        return u'{}: №{} {} - {}'.format(
            self.reader.username, self.book_item.pk,
            self.book_item.book.author,
            self.book_item.book.name
        )
    
    class Meta:
        verbose_name = u"Empréstimo"
        verbose_name_plural = u"Empréstimos"

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
