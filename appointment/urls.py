from django.urls import path
from .views import assign_patient_to_doctor,get_appointment,get_specififc_appointment,delete_appointment

urlpatterns = [
    path('create_appointment/',assign_patient_to_doctor, name='create_appointment'),
    path('get_appointment/',get_appointment,name='get_appointment'),
    path('get_specific_appointment/<int:pk>/', get_specififc_appointment, name='get_specific_appointment'),
    path('delete_appointment/<int:pk>/', delete_appointment, name='delete_appointment')


]
