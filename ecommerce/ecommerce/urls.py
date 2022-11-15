from django.conf import settings
from django.conf.urls import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path, re_path
from django.utils.translation import gettext_lazy as _
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

# swagger schema view
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

    # api urls
    path('address', include('address.urls')),
    path('members/', include('members.urls')),
    path('product/', include('produit.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # tokens urls
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),

    # swagger urls
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
                                               cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
                                             cache_timeout=0), name='schema-redoc'),

    # authentication urls
    path('oauth/', include('social_django.urls',
         namespace='social_log')),  # <-- here
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

    path('dj-rest-auth/', include('dj_rest_auth.urls')),


)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
