from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils.translation import gettext_lazy as _

from address.models import Address


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """

        if not email:
            raise ValueError('Users must have an email address')

        if not username:
            raise ValueError('Users must have an username address')

        user = self.model(
            username=username,
            email=email,
        )

        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, username, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(verbose_name=_(
        'Username'), max_length=50, unique=True)
    email = models.EmailField(
        verbose_name=_('email address'), max_length=150, unique=True)
    firstname = models.CharField(verbose_name=_(
        'first name'), max_length=50, null=True, blank=True)
    lastname = models.CharField(verbose_name=_(
        'last name'), max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(
        verbose_name=_('date of birth'), null=True)
    phone = models.CharField(verbose_name=_(
        'Phone Number'), max_length=20, null=True, blank=True)

    is_active = models.BooleanField(verbose_name=_('Active'), default=True)
    is_admin = models.BooleanField(verbose_name=_('admin'), default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f'{self.username}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return f'{self.is_admin}'

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ["id"]


class UserAdress(models.Model):
    ADDRESS_TYPE = (
        ("facturation", _("billing")),
        ("import", _("Import")),
        ("export", _("Export")),
        ("livraison", _("delivery")),
        ("siege social", _("headquarters"))
    )
    user = models.ForeignKey(MyUser, verbose_name=_("username"),
                             on_delete=models.CASCADE)
    address = models.ForeignKey(Address,
                                verbose_name=_('address'),
                                on_delete=models.DO_NOTHING,
                                )

    address_type = models.CharField(verbose_name=_('address type'),
                                    max_length=50, choices=ADDRESS_TYPE)
    active = models.BooleanField(verbose_name=_('active'), default=True)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = _('User Address')
        verbose_name_plural = _('User Address')
