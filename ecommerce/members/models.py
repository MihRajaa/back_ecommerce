from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils.translation import gettext as _

from adresse.models import Adresse


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
        'User name'), max_length=50, unique=True)
    email = models.EmailField(
        verbose_name=_('email address'), max_length=150)
    firstname = models.CharField(verbose_name=_('first name'), max_length=50)
    lastname = models.CharField(verbose_name=_('last name'), max_length=50)
    date_of_birth = models.DateField(
        verbose_name=_('date of birth'), null=True)
    phone = models.CharField(verbose_name=_('Phone Number'), max_length=20)

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


class UserAdress(models.Model):
    ADRESSE_TYPE = (
        ("facturation", _("Facturation")),
        ("import", _("Import")),
        ("export", _("Export")),
        ("livraison", _("Livraison")),
        ("siege social", _("Siege Social"))
    )
    user = models.ForeignKey(MyUser, verbose_name=_("utilisateur"),
                             on_delete=models.CASCADE)
    adresse = models.ForeignKey(Adresse, verbose_name=_(
        'adresse'), on_delete=models.DO_NOTHING)

    adresse_type = models.CharField(verbose_name=_('type adresse'),
                                    max_length=50, choices=ADRESSE_TYPE)
    active = models.BooleanField(verbose_name=_('active'), default=True)

    def __str__(self):
        return f'{self.user}'
