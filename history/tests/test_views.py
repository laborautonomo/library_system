# encoding: utf-8

from datetime import date

from django.core.urlresolvers import reverse
from django.test import TestCase

from books.models import Book, BookItem
from history.models import HistoryItem
from readers.models import Reader


class TestBookListView(TestCase):
    def test_total_fine(self):
        reader1 = Reader.objects.get_or_create(username="user")[0]
        reader1.set_password('user')
        reader1.save()

        book1 = Book.objects.get_or_create(name="Três corações", author="Jack. Londres",
                                           year=2010, publisher="Astrel")[0]
        book_i1 = BookItem.objects.get_or_create(book=book1)[0]
        HistoryItem.objects.get_or_create(date_taken=date(2015, 11, 1), date_due=date(2015, 11, 6),
                                          date_returned=date(2015, 11, 9), daily_fine=10,
                                          book_item=book_i1, reader=reader1)

        self.client.login(username='user', password='user')
        response = self.client.get(reverse('book_list'))
        self.assertContains(response, '30')
