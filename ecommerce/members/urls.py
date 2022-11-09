from django.urls import path
from django.contrib.auth import views as auth_views

from .views import HomeView, MemberRegister

app_name = 'members'

urlpatterns = [
    path('register/', MemberRegister.as_view(),
         name='registration'),
    # Login and Logout
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', HomeView, name="home"),
]
