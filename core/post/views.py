from rest_framework import viewsets
from rest_framework import permissions
from post.serializers import ZamowieniaSerializer
from post.models import Zamowienia

class ZamowieniaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Zamowienia.objects.all()
    serializer_class = ZamowieniaSerializer
    permission_classes = [permissions.DjangoModelPermissions]
