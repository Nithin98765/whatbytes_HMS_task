from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'phone','specilaization', 'experience_years', 'consulation_fee', 'is_active']

    read_only_fields = ['id', 'is_active']

    def create(self, validated_data):
        user = self.context['request'].user
        return Doctor.objects.create(user=user, **validated_data)