from django.urls import path
from django.utils.translation import gettext_lazy as _

from .views import MemberRegister

app_name = 'members'

urlpatterns = [
    path(_('register/'), MemberRegister.as_view()),
]
