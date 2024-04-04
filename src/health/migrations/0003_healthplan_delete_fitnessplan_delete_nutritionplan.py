# Generated by Django 5.0.3 on 2024-04-04 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0002_fitnessplan_nutritionplan_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('plan_type', models.CharField(choices=[('Fitness', 'Fitness'), ('Nutrition', 'Nutrition')], max_length=20)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='health_files/plans/')),
                ('tags', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='FitnessPlan',
        ),
        migrations.DeleteModel(
            name='NutritionPlan',
        ),
    ]
