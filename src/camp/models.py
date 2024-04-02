from django.db import models

class Camp(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    tags = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.title} - {self.start_date}"
