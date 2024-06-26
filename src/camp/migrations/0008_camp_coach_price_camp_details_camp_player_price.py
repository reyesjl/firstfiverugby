# Generated by Django 5.0.3 on 2024-04-19 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0007_camp_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='coach_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='camp',
            name='details',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='camp',
            name='player_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
