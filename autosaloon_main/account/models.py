from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime, timedelta, timezone
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, Permission
from account.manager import CustomUserManager
from autosaloon_api.models import Saloon

USER_ROLE = (
    ('Customer', 'Customer'),
    ('Staff', 'Staff'),
    ('Admin', 'Admin'),
    ('SuperAdmin', 'SuperAdmin'),
)

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    saloon = models.ForeignKey(Saloon, on_delete=models.CASCADE)
    email = models.EmailField(
        _('email address'), null=True, blank=True, unique=True)
    firstname = models.CharField(max_length=255,)
    lastname = models.CharField(max_length=255,)
    password = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=50, choices=GENDER, blank=True)
    phone = models.CharField(max_length=17, blank=True, null=True)
    roles = models.CharField(max_length=20, blank=True,choices=USER_ROLE, default=['Customer'])
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        ordering = ('-date_joined',)
    def __str__(self):
        return f'{self.firstname} {self.email}'

