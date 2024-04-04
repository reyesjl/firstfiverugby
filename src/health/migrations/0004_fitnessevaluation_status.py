# Generated by Django 5.0.3 on 2024-04-04 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_healthplan_delete_fitnessplan_delete_nutritionplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='fitnessevaluation',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Under Review', 'Under Review'), ('Completed', 'Completed')], default='Pending', max_length=20),
        ),
    ]