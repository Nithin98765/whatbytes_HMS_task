from django.db import models
from patients.utils import TimeStampedModel
from django.conf import settings
from accounts.models import User
from django.core.validators import MinValueValidator

# Create your models here.
class Doctor(TimeStampedModel):
    class Specilaization(models.TextChoices):
        CARDIOLOGY = "Cardiology", "Cardiology"
        NEUROLOGY = "Neurology", "Neurology"
        ORTHOPEDICS = "Orthopedics", "Orthopedics"
        GENERAL = "General", "General"
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctors')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    specilaization = models.CharField(max_length=50, choices=Specilaization.choices)
    experience_years = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    consulation_fee = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        indexes=[models.Index(fields=['phone'])]

    def __str__(self):
        return self.name
    

