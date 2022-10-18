from rest_framework import viewsets

from .models import *
from .serializers import *

# Create your views here.


class GouvernatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows governorate to be viewed or edited.
    """

    queryset = Gouvernat.objects.all().order_by('governorate')
    serializer_class = GouvernatSerializer


class VilleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows city to be viewed or edited.
    """

    queryset = Ville.objects.all().order_by('city')
    serializer_class = VilleSerializer


class CodePosteViewSet(viewsets.ModelViewSet):
    queryset = CodePoste.objects.all()
    serializer_class = CodePosteSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class LocaliteViewSet(viewsets.ModelViewSet):
    queryset = Localite.objects.all()
    serializer_class = LocaliteSerializer
