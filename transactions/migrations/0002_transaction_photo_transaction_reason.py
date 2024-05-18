# Generated by Django 4.2 on 2024-05-17 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='transaction_photos/'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='reason',
            field=models.TextField(blank=True),
        ),
    ]
