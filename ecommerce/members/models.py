from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils.translation import gettext as _


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
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(
        verbose_name=_('email address'), max_length=150)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True)
    phone = models.CharField(max_length=20)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

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
    ACTIVE_TYPE = (
        ("Admin", _("Administrateur")),
        ("User", _("Utilisateur"))
    )
    user = models.ForeignKey(MyUser, verbose_name=_("utilisateur"),
                             on_delete=models.CASCADE)
    user_type = models.CharField(max_length=50, choices=ACTIVE_TYPE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user}'
