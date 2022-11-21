from django.urls import path, include
from django.contrib.auth import views as auth_views

from rest_framework.routers import DefaultRouter

from .views import MemberRegister, MyUserViewSet, UserAdressViewSet, settings, password


app_name = 'members'

router = DefaultRouter()

router.register('myuser', MyUserViewSet),
router.register('UserAdress', UserAdressViewSet),


urlpatterns = [

    path('', include(router.urls)),

    path('register/', MemberRegister.as_view(), name='registration'),

    path('settings/', settings, name='settings'),
    path('settings/password/', password, name='password'),

    # Login and Logout
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
