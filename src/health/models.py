from django.db import models

class FitnessEvaluation(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Under Review', 'Under Review'),
        ('Completed', 'Completed'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    workout_or_meal_plan = models.FileField(upload_to='health_files/fitness_evaluations/')
    goals_description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class HealthPlan(models.Model):
    PLAN_TYPES = (
        ('Fitness', 'Fitness'),
        ('Nutrition', 'Nutrition'),
    )
    
    title = models.CharField(max_length=100)
    plan_type = models.CharField(max_length=20, choices=PLAN_TYPES)
    author = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='health_files/plans/')
    tags = models.CharField(max_length=255, blank=True)