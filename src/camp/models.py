from django.db import models
from django.utils import timezone

class Camp(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=150, blank=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    tags = models.CharField(max_length=255, blank=True)
    details = models.TextField(default='')
    coach_price = models.IntegerField(blank=True, null=True)
    player_price = models.IntegerField(blank=True, null=True)
    coach_payment_link = models.CharField(max_length=255, blank=True)
    player_payment_link = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.title} - {self.start_date}"
    
class GeneralRegistration(models.Model):
    CAMP_REGISTER_TYPE_CHOICES = [
        ('coach', 'Coach'),
        ('player', 'Player'),
    ]
    camp = models.ForeignKey(Camp, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=CAMP_REGISTER_TYPE_CHOICES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    club = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    birthday = models.DateField(blank=True, null=True)
    emergency_contact_first_name = models.CharField(max_length=100)
    emergency_contact_last_name = models.CharField(max_length=100)
    emergency_contact_email = models.EmailField()
    emergency_contact_phone = models.CharField(max_length=20)
    photo_release_form = models.FileField(upload_to='camp_files/photo_release_forms/', blank=True)
    liability_waiver = models.FileField(upload_to='camp_files/liability_waivers/', blank=True)
    registration_date = models.DateTimeField(default=timezone.now)
    has_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.camp.title} - {self.type} : {self.has_paid}"
    
class CampRegistration(models.Model):
    camp = models.ForeignKey(Camp, on_delete=models.CASCADE)
    player_first_name = models.CharField(max_length=100)
    player_last_name = models.CharField(max_length=100)
    player_birthday = models.DateField()
    player_club = models.CharField(max_length=100)
    player_position = models.CharField(max_length=100)
    emergency_contact_first_name = models.CharField(max_length=100)
    emergency_contact_last_name = models.CharField(max_length=100)
    emergency_contact_email = models.EmailField()
    emergency_contact_phone = models.CharField(max_length=20)
    photo_release_form = models.FileField(upload_to='camp_files/photo_release_forms/')
    liability_waiver = models.FileField(upload_to='camp_files/liability_waivers/')
    registration_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.player_first_name} {self.player_last_name} - {self.camp.title}"
    
class CoachCampRegistration(models.Model):
    camp = models.ForeignKey(Camp, on_delete=models.CASCADE)
    coach_first_name = models.CharField(max_length=100)
    coach_last_name = models.CharField(max_length=100)
    coach_email = models.EmailField()
    coach_phone = models.CharField(max_length=20)
    coach_club = models.CharField(max_length=100)
    registration_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.coach_first_name} {self.coach_last_name} - {self.camp.title}"
