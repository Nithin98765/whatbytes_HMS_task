from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields ='__all__'
        read_only_fields=['id', 'status']

    def validate(self, data):
        doctor = data.get("doctor")
        date = data.get('appointment_date')
        time = data.get('appointment_time')

        if Appointment.objects.filter(doctor=doctor,appointment_date=date,appointment_time=time,status="Scheduled").exists():
            raise serializers.ValidationError("Doctor Already has appointment at this time")
        
        return data
    
    