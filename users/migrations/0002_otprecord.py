# Generated by Django 4.1.6 on 2023-02-14 15:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtpRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=16)),
                ('otp', models.PositiveIntegerField()),
                ('attempts', models.PositiveIntegerField(default=1)),
                ('is_applied', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='general.country')),
            ],
            options={
                'verbose_name': 'Otp Record',
                'verbose_name_plural': 'Otp Records',
                'db_table': 'users_otp_record',
                'ordering': ('-date_added',),
            },
        ),
    ]
