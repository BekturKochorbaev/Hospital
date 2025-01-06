from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import *


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('username', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


# Teacher Serializer
class DoctorFormSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = DoctorProfile

    def create(self, validated_data):
        return DoctorProfile.objects.create_user(**validated_data)


# Student Serializer
class PatientFormSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = PatientProfile

    def create(self, validated_data):
        return PatientProfile.objects.create_user(**validated_data)


# Base Login Serializer
class BaseLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Invalid credentials')

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class DoctorLoginSerializer(BaseLoginSerializer):
    pass


# Student Login Serializer
class PatientLoginSerializer(BaseLoginSerializer):
    pass


class DoctorProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = ['id', 'first_name', 'last_name', 'profile_picture', "specialty", 'gender', 'phone_number', 'department', 'shift_start',
                  'shift_end', 'working_days', 'qualification']


class DoctorScheduleSerializers(serializers.ModelSerializer):

    class Meta:
        model = DoctorProfile
        fields = ['first_name', 'last_name', 'profile_picture',  "specialty", 'shift_end', 'shift_start', 'working_days']


class PatientProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = ['id', 'first_name', 'last_name', 'blood_type', 'date_of_birth', 'allergies', 'medical_history',
                  'phone_number', 'address', 'gender']




