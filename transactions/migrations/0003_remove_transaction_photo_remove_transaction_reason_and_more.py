# Generated by Django 4.2 on 2024-05-18 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_transaction_photo_transaction_reason'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='reason',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='receiver',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='sender',
            field=models.CharField(max_length=100),
        ),
    ]
