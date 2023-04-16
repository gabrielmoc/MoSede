# Generated by Django 4.2 on 2023-04-16 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosede', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wine_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
    ]
