# En tu forms.py dentro de la aplicación accounts

from django import forms
from accounts.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['card_number']  # Campos que quieres mostrar en el formulario

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['card_number'].required = False  # Hacer el campo opcional

# En tu forms.py dentro de la aplicación accounts


from django import forms
from django.contrib.auth.models import User
from .models import Transaction   # Assuming the models.py file is in the same directory

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['receiver', 'amount', 'sender']
from django.db import models

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)

class TransferForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['receiver', 'amount']

