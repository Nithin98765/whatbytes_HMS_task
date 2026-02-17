from django.urls import path
from .views import create_patient, list_patients, get_specific_patient,update_patient, delete_patient

urlpatterns = [
    path('create/', create_patient, name='create_patient'),
    path('list_patients/',list_patients, name='list-patients'),
    path('get_specific_patient/<int:pk>/',get_specific_patient, name="get_specific-patient"),
    path("patients/<int:pk>/update/", update_patient, name="update-patient"),
    path("patients/<int:pk>/delete/", delete_patient, name="delete-patient"),


]
