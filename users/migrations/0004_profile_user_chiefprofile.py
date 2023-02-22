# Generated by Django 4.1.6 on 2023-02-21 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_profile_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ChiefProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('auto_id', models.PositiveIntegerField(db_index=True, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=128)),
                ('user_name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=128)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('password', models.TextField(blank=True, null=True)),
                ('profile_type', models.CharField(blank=True, choices=[('product_manager', 'Product Manager')], max_length=128, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Chief Profile',
                'verbose_name_plural': 'Chief Profiles',
                'db_table': 'users_chief_profile',
                'ordering': ('-date_added',),
            },
        ),
    ]