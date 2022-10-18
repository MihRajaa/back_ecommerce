from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from address import views as address_views
from members import views as member_views
from produit import views as produit_views

router = routers.DefaultRouter()
router.register(r'governorate', address_views.GouvernatViewSet)
router.register(r'city', address_views.VilleViewSet)
router.register(r'code postal', address_views.CodePosteViewSet)
router.register(r'localite', address_views.LocaliteViewSet)
router.register(r'address', address_views.AddressViewSet)

router.register(r'myuser', member_views.MyUserViewSet)
router.register(r'useraddress', member_views.UserAddressViewSet)

router.register(r'produit', produit_views.ProduitViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="E-Commerce",
        default_version='v0.1',
        description="Ecommerce Backend ",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = i18n_patterns(

    path(_('admin/'), admin.site.urls),
    path('', include(router.urls)),
    path('', include('members.urls')),
    path('api-auth/', include('rest_framework.urls')),

    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
                                               cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
                                             cache_timeout=0), name='schema-redoc'),

)
