from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from adresse import views

router = routers.DefaultRouter()
router.register(r'gouvernat', views.GouvernatViewSet)
router.register(r'ville', views.VilleViewSet)
router.register(r'code postal', views.CodePosteViewSet)
router.register(r'localite', views.LocaliteViewSet)
router.register(r'adresse', views.AdresseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
