from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions', blank=True)

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BankAccount(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.account_number









class SpecialUserGroup(Group):
    class Meta:
        proxy = True
        verbose_name = 'Special User'
        verbose_name_plural = 'Special Users'

from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Agrega cualquier otro campo que desees en tu perfil de usuario

    card_number = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return self.user.username




class Transaction(models.Model):
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)  # Agrega este campo
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.sender} to {self.receiver}: {self.amount}"
