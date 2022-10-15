from django.urls import path
from .views import MemberRegister

app_name = 'members'

urlpatterns = [
    path('register/', MemberRegister.as_view()),
]
