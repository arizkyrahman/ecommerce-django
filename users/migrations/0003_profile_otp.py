# Generated by Django 4.1.6 on 2023-02-15 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_otprecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='otp',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
