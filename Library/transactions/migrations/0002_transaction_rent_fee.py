# Generated by Django 4.1.7 on 2024-01-03 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='rent_fee',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
