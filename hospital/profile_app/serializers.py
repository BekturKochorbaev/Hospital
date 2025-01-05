from rest_framework import serializers
from .models import *


class DoctorProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = ['id', 'first_name', 'last_name', 'profile_picture', "specialty", 'gender', 'phone_number', 'department', 'shift_start',
                  'shift_end', 'working_days', 'qualification']


class DoctorScheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = ['first_name', 'last_name', 'profile_picture',  "specialty", 'shift_end', 'shift_start', 'working_days',]


class PatientProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = ['id', 'first_name', 'last_name', 'blood_type', 'date_of_birth', 'allergies', 'medical_history',
                  'phone_number', 'address', 'gender']




