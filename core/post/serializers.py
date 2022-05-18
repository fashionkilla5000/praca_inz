from rest_framework import serializers
from post.models import Zamowienia

class ZamowieniaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Zamowienia
        fields = ['id','data','adres','platforma','platnosc','kwota','telefon','komentarz','status','pracownikId']