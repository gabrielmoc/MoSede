# Generated by Django 4.2 on 2023-04-17 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosede', '0006_remove_user_is_active_remove_user_is_staff_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]