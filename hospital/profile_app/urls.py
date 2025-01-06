from django.urls import path
from .views import *

urlpatterns = [
    path('register_doctor/', DoctorRegisterView.as_view(), name='register'),
    path('login_doctor/', DoctorCustomLoginView.as_view(), name='login'),
    path('logout_doctor/', DoctorLogoutView.as_view(), name='logout'),

    path('doctor_profile/<int:pk>/', DoctorProfileDetailAPIView.as_view(), name='doctor_profile_list'),
    path('doctor_schedule/', DoctorScheduleListAPIView.as_view(), name='doctor_profile_create'),
    path('doctor_schedule_create/', DoctorScheduleCreateAPIView.as_view(), name='doctor_schedule_create'),

    path('patient_profile_list/', PatientProfileListAPIView.as_view(), name='patient_profile_list'),
    path('patient_profile_create/', PatientProfileCreateAPIView.as_view(), name='patient_profile_create')

]