from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import *

app_name = "address"

router = DefaultRouter()
router.register('governorate', GouvernatViewSet)
router.register('city', VilleViewSet)
router.register('code postal', CodePosteViewSet)
router.register('localite', LocaliteViewSet)
router.register('address',  AddressViewSet)

urlpatterns = [
    path('', include(router.urls))
]
