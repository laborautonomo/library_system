# -- coding: utf-8 --
from django.test import TestCase
from django.core.urlresolvers import reverse
from readers.models import Reader


class TestLogout(TestCase):
    def test_logout(self):
        reader1 = Reader.objects.get_or_create(username="user")[0]
        reader1.set_password('user')
        reader1.save()
        self.client.login(username='user', password='user')
        response = self.client.get(reverse('logout'))
        self.assertContains(response, 'Até mais :)')
