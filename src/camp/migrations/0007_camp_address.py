# Generated by Django 5.0.3 on 2024-04-19 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0006_generalregistration'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='address',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]