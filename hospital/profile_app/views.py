from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from rest_framework.response import Response


class BaseRegisterView(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



# Teacher Register View
class DoctorRegisterView(BaseRegisterView):
    serializer_class = DoctorFormSerializer


# Student Register View
class PatientRegisterView(BaseRegisterView):
    serializer_class = PatientFormSerializer


# Base Custom Login View
class BaseCustomLoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Teacher Login View
class DoctorCustomLoginView(BaseCustomLoginView):
    serializer_class = DoctorLoginSerializer


# Student Login View
class PatientCustomLoginView(BaseCustomLoginView):
    serializer_class = PatientLoginSerializer


# Base Logout View
class BaseLogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


# Teacher Logout View
class DoctorLogoutView(BaseLogoutView):
    pass


# Student Logout View
class PatientLogoutView(BaseLogoutView):
    pass


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class DoctorProfileDetailAPIView(generics.RetrieveAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializers
    pagination_class = Pagination


class DoctorScheduleListAPIView(generics.ListAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorScheduleSerializers
    pagination_class = Pagination


class DoctorScheduleCreateAPIView(generics.CreateAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorScheduleSerializers



class PatientProfileListAPIView(generics.ListAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializers

    def get_queryset(self):
        return PatientProfile.objects.filter(id=self.request.user.id)


class PatientProfileCreateAPIView(generics.CreateAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializers

    def get_queryset(self):
         return DoctorProfile.objects.filter(id=self.request.user.id)




