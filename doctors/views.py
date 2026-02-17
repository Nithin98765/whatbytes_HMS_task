from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import DoctorSerializer
from rest_framework import status
from .models import Doctor

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_doctor(request):
    serializer = DoctorSerializer(data=request.data, context={'request':request})

    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Successfully created"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_doctors(request):
    doctors = Doctor.objects.filter(user=request.user,is_active=True)
    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

def get_doctor_object(pk, request):
    try:
        return Doctor.objects.get(pk=pk, user=request.user, is_active=True)
    except Doctor.DoesNotExist:
        return None

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_specific_doctor(request, pk):
    doctor = get_doctor_object(pk, request)
    if not doctor:
        return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = DoctorSerializer(doctor)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_doctor(request, pk):
    doctor = get_doctor_object(pk, request)
    if not doctor:
        return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = DoctorSerializer(doctor, data=request.data, partial=False)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_doctor(request, pk):
    doctor = get_doctor_object(pk, request)
    if not doctor:
        return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)
    
    doctor.is_active = False
    doctor.save()
    return Response({"message": "Doctor deleted sucessfully"}, status=status.HTTP_204_NO_CONTENT)


    

