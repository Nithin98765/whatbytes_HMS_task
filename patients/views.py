from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Patient
from .serializers import PatientSerializer

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_patient(request):
    serializer = PatientSerializer(data=request.data, context={'request':request})

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_patients(request):
    patients = Patient.objects.filter(user=request.user, is_active=True).order_by('name')
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def get_patient_or_404(pk, user):
    """Helper function to retrieve patient or return 404 response"""
    try:
        return Patient.objects.get(pk=pk, user=user, is_active=True)
    except Patient.DoesNotExist:
        return None

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_specific_patient(request, pk):
    patient = get_patient_or_404(pk, request.user)
    if not patient:
        return Response(
            {"error": "Patient not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    serializer = PatientSerializer(patient)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_patient(request, pk):
    patient = get_patient_or_404(pk, request.user)
    if not patient:
        return Response(
            {"error": "Patient not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    serializer = PatientSerializer(patient, data=request.data, partial=False)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_patient(request, pk):
    patient = get_patient_or_404(pk, request.user)
    if not patient:
        return Response(
            {"error": "Patient not found"},
            status=status.HTTP_404_NOT_FOUND
        )
    patient.is_active = False
    patient.save()
    return Response({"message": "Patient Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT)

