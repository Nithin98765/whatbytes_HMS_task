from django.db import models
from patients.models import Patient
from patients.utils import TimeStampedModel
from doctors.models import Doctor

# Create your models here.
class Appointment(TimeStampedModel):
    class Status(models.TextChoices):
        SCHEDULED = "Scheduled", "Scheduled"
        COMPLETED = "Completed", "Completed"
        CANCELLED = "Cancelled", "Cancelled"

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,related_name='appointments')
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='appointments')
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.SCHEDULED)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-appointment_date", "-appointment_time"]
        unique_together = ["doctor", "patient", "appointment_date", "appointment_time"]

    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name} ({self.appointment_date})"
