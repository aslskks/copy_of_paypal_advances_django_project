from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission

class CustomUser(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions', blank=True)

class BankAccount(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    account_number = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.account_number}'



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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Agrega cualquier otro campo que necesites para tu transacción

    def __str__(self):
        return f"Transaction for {self.user.username}"