from django.urls import path
from .views import *

urlpatterns = [
    path('doctor_profile_list/', DoctorProfileListAPIView.as_view(), name='doctor_profile_list'),
    path('doctor_schedule/', DoctorScheduleListAPIView.as_view(), name='doctor_profile_create'),

    path('patient_profile_list/', PatientProfileListAPIView.as_view(), name='patient_profile_list'),
    path('patient_profile_create/', PatientProfileCreateAPIView.as_view(), name='patient_profile_create')

]