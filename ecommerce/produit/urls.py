from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

app_name = 'product'

router = DefaultRouter()
router.register('product', ProduitViewSet)


urlpatterns = [
    path('', include(router.urls))
]
