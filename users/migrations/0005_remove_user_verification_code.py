# Generated by Django 4.2.7 on 2024-01-14 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_is_active_alter_user_verification_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='verification_code',
        ),
    ]
