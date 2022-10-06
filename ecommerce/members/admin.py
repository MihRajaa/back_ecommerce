from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import *


class MyUserCreationForm(forms.ModelForm):
    """A form for creating new user. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('username', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class MyUserChangeForm(forms.ModelForm):
    """A form for updating user. Includes all the fields on
    the Myuser, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'firstname', 'lastname',
                  'date_of_birth', 'phone', 'password', 'is_active', 'is_admin')


@admin.register(MyUser)
class MyUserAdmin(BaseUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm

    list_display = ('username', 'email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (

        ("exemple", {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'firstname',
         'lastname', 'date_of_birth', 'phone',)}),
        ('Permissions', {'fields': ('is_admin', )}),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()


@admin.register(UserAdress)
class UserAdressAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Group)
