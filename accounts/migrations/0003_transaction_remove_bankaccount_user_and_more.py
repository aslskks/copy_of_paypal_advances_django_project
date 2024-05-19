from django.db import migrations, models
from django.contrib.auth.models import User

def set_default_owner(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    default_user, created = User.objects.get_or_create(username='default_user', defaults={'password': 'default_password'})
    BankAccount = apps.get_model('accounts', 'BankAccount')
    BankAccount.objects.filter(owner__isnull=True).update(owner=default_user)

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_specialusergroup_customuser_address_customuser_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccount',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=models.CASCADE, to='auth.User'),
        ),
        migrations.RunPython(set_default_owner),
    ]
