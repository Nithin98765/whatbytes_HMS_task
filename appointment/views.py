from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from .serializers import AppointmentSerializer
from .models import Appointment

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assign_patient_to_doctor(request):
    serializer = AppointmentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_appointment(request):
    appointment = Appointment.objecst.all()
    serializer = AppointmentSerializer(appointment, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_specififc_appointment(request, pk):
    try:
        appointment = Appointment.objects.get(pk=pk)
    except Appointment.DoesNotExist:
        return Response({"error":"Appointment not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = AppointmentSerializer(appointment)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_appointment(request, pk):
    try:
        appointment = Appointment.objects.get(pk=pk)
    except Appointment.DoesNotExist:
        return Response({"error":"Appointment not found"}, status=status.HTTP_404_NOT_FOUND)
    
    appointment.status = "Cancelled"
    appointment.save()
    return Response({'message':"appointment Cancelled"},status=status.HTTP_204_NO_CONTENT)




