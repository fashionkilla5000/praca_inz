from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Zamowienia)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','data','adres','platforma','platnosc','kwota','telefon','komentarz','status','pracownikId')