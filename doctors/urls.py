from django.urls import path
from .views import create_doctor,list_doctors,get_specific_doctor, update_doctor, delete_doctor

urlpatterns = [
    path('create/', create_doctor, name='create_doctor'),
    path('list_doctors/',list_doctors, name='list_doctors'),
    path('get_specific_doctor/<int:pk>/',get_specific_doctor, name="get_specific_doctor"),
    path("update/<int:pk>/", update_doctor, name="update-doctor"),
    path("delete/<int:pk>/", delete_doctor, name="delete-doctor"),


]
