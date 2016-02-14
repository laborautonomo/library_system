# -*- coding: utf-8 -*-

from django.db.models.query import EmptyQuerySet
from django.views.generic import ListView

from history.models import HistoryItem


class BookListView(ListView):
    model = HistoryItem
    template_name = 'book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        if self.request.user.is_authenticated():
            return super(BookListView, self).get_queryset().filter(reader=self.request.user)
        else:
            return EmptyQuerySet

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        total_fine = 0
        if self.get_queryset() != EmptyQuerySet:
            for item in self.get_queryset():
                if item.fine > 0 and not item.is_fine_paid:
                    total_fine = total_fine + item.fine
            context['total_fine'] = total_fine
        return context
