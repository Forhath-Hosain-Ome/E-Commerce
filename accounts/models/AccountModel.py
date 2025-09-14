from django.db import models
from django.contrib.auth.models import AbstractUser
from .MyAccountManager import MyAccountManager

class Account(AbstractUser):
    phone_number = models.CharField(max_length=50)
    
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default = False)

    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyAccountManager

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True