from django.db import models

class TourQuote(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Under Review', 'Under Review'),
        ('Completed', 'Completed'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    club_name = models.CharField(max_length=200)
    club_size = models.PositiveIntegerField()
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Tour Quote - {self.first_name} {self.last_name} from {self.club_name}"
