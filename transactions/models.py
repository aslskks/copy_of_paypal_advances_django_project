from django.db import models
from accounts.models import BankAccount

class Transaction(models.Model):
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)  # Agrega este campo
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.sender} to {self.receiver}: {self.amount}"
