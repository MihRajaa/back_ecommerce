from rest_framework import viewsets

from .models import *
from .serializers import *

# Create your views here.


class GouvernatViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows gouvernat to be viewed or edited.
    """

    queryset = Gouvernat.objects.all().order_by('gouvernat')
    serializer_class = GouvernatSerializer


class VilleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ville to be viewed or edited.
    """

    queryset = Ville.objects.all().order_by('ville')
    serializer_class = VilleSerializer


class CodePosteViewSet(viewsets.ModelViewSet):
    queryset = CodePoste.objects.all()
    serializer_class = CodePosteSerializer


class AdresseViewSet(viewsets.ModelViewSet):
    queryset = Adresse.objects.all()
    serializer_class = AdresseSerializer


class LocaliteViewSet(viewsets.ModelViewSet):
    queryset = Localite.objects.all()
    serializer_class = LocaliteSerializer
