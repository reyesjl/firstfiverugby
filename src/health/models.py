from django.db import models

class FitnessEvaluation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    workout_or_meal_plan = models.FileField(upload_to='health_files/')
    goals_description = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
