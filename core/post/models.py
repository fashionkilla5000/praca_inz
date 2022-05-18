from django.db import models
from django.conf import settings
from django.utils import timezone

class Zamowienia(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateTimeField(default=timezone.now,editable=False)
    adres = models.CharField(max_length=50, null = False)

    opcje_platnosc = (
        ('karta','Karta'),
        ('gotowka','Gotowka'),
        ('zaplacone','Zaplacone')
    )
    platnosc = models.CharField(max_length=10, choices=opcje_platnosc, default='zaplacone')

    kwota = models.CharField(max_length=5, null = False)
    telefon = models.CharField(max_length=12)
    komentarz = models.CharField(max_length=200, null=True, blank=True)

    opcje_platforma = (
        ('uber','Uber'),
        ('rest','Rest'),
        ('glovo','Glovo'),
        ('tel','Tel')
    )
    platforma = models.CharField(max_length=5, choices=opcje_platforma, default='glovo')

    opcje_status = (
        ('oczekujacy','Oczekujacy'),
        ('w trakcie', 'W trakcie'),
        ('zakonczony','Zakonczony')
    )
    status = models.CharField(max_length=10, choices=opcje_status, default='oczekujacy', editable=False)

    pracownikId = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='dostawca', on_delete=models.CASCADE, editable=False, null=True)


    def __str__(self):
        return self.adres

    class Meta:
        ordering = ['data']
