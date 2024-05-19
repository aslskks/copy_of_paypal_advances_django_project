# transactions/models.py
from django.db import models
from django.core.exceptions import ValidationError
from accounts.models import UserProfile
from django.utils import timezone

class BankAccount(models.Model):
    owner = models.ForeignKey('accounts.UserProfile', on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.owner}'s Bank Account"

def validate_account_default(value):
    if value == 'cambia esto':
        raise ValidationError('Por favor, selecciona un valor distinto para el campo account.')

class Transaction(models.Model):
    sender = models.ForeignKey(UserProfile, related_name='sent_transactions', on_delete=models.CASCADE)
    receiver = models.ForeignKey(UserProfile, related_name='received_transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    # El campo account se hace opcional permitiendo valores nulos
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE, default=None)

    timestamp = models.DateTimeField(default=timezone.now)  # Agregar este campo con el valor predeterminado

    def __str__(self):
        return f'{self.sender.user.username} -> {self.receiver.user.username} (${self.amount})'

