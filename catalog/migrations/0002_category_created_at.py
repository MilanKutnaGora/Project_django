# Generated by Django 4.2.7 on 2023-11-30 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.TextField(default=1, verbose_name='создание'),
            preserve_default=False,
        ),
    ]
