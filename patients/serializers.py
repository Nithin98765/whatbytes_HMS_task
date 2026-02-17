from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Patient
        fields = ["id",
                  'name',
                  'gender',
                  'phone',
                  'address',
                  'blood_group',
                  'dob',
                  'reason_for_visit',
                  'is_active',
                  'age'
        ]
        read_only_fields = ['id','is_active']

    
    def get_age(self, obj):
        return obj.calculate_age()
    
    def create(self, validated_data):
        user = self.context['request'].user
        return Patient.objects.create(user=user, **validated_data)