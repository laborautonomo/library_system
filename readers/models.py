# -- coding: utf-8 --
from django.contrib.auth.models import User, UserManager
from django.db import models


# noinspection PyAbstractClass
class Reader(User):
    phone_number = models.CharField(blank=True, verbose_name="Telefone", max_length=16)
    address = models.CharField(verbose_name="Endereço", blank=True, max_length=50)
    objects = UserManager()

    def __unicode__(self):
        return u'№{} {} {}: {}'.format(
            self.pk, self.first_name,
            self.last_name,
            self.username
        )
    
    class Meta:
        verbose_name = u"Usuári@"
        verbose_name_plural = u"Usuári@s"