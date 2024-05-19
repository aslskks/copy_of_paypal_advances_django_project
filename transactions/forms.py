from django import forms
from transactions.models import Transaction
from accounts.models import UserProfile

class TransferForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['receiver', 'amount']

    def __init__(self, user, *args, **kwargs):
        super(TransferForm, self).__init__(*args, **kwargs)
        self.fields['receiver'].queryset = UserProfile.objects.exclude(user=user.user)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['balance']  # Asegúrate de que los campos aquí existan en UserProfile


from django.db import models
from accounts.models import User

class TransactionForm(forms.ModelForm):  # Renombrado a TransactionForm
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
