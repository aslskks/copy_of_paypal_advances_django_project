# accounts/models.py
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

# models.py
from django.db import models
from django.contrib.auth.models import User

class BankAccount(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    # aqui creo que tambien puedes poner el account_number

class Transaction(models.Model):
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(max_length=10, choices=[('deposit', 'Deposit'), ('withdrawal', 'Withdrawal')])



class SpecialUserGroup(Group):
    class Meta:
        proxy = True
        verbose_name = 'Special User'
        verbose_name_plural = 'Special Users'

# accounts/models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.user.username




