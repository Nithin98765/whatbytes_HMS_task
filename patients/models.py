from django.db import models
from accounts.models import User
from django.conf import settings
from datetime import date
from .utils import TimeStampedModel

# Create your models here.
class Patient(TimeStampedModel):
    class Gender(models.TextChoices):
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"
        OTHERS = "Others", "Others"
    
    class BloodGroup(models.TextChoices):
        A_POS = "A+", "A+"
        A_NEG = "A-", "A-"
        B_POS = "B+", "B+"
        B_NEG = "B-", "B-"
        O_POS = "O+", "O+"
        O_NEG = "O-", "O-"
        AB_POS = "AB+", "AB+"
        AB_NEG = "AB-", "AB-"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patients')
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10,choices=Gender.choices)
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True)
    blood_group = models.CharField(max_length=5, choices=BloodGroup.choices, blank=True)
    dob = models.DateField()
    reason_for_visit = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['phone'])
        ]

    def calculate_age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day)<(self.dob.month, self.dob.day))

    def __str__(self):
        return self.name