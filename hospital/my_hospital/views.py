from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets, generics


class DepartmentListAPIView(generics.ListAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializers


class DepartmentListAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializers


class AppointmentListAPIView(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentListSerializers


class AppointmentCreateAPIView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentCreateSerializers


class AppointmentDetailDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentListSerializers


class MedicalRecordListAPIView(generics.ListAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordListSerializers


class MedicalRecordCreateAPIView(generics.CreateAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordCreateSerializers


class MedicalRecordDetailDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordListSerializers


class PrescriptionListAPIView(generics.ListAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionListSerializers


class PrescriptionDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionListSerializers


class PrescriptionCreateAPIView(generics.CreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionListSerializers


class BillingsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Billings.objects.all()
    serializer_class = BillingsListCreateSerializers


class BillingsDetailDeleteCreateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Billings.objects.all()
    serializer_class = BillingsListCreateSerializers


class WardsListAPIView(generics.ListAPIView):
    queryset = Wards.objects.all()
    serializer_class = WardsListSerializers


class WardsCreateAPIView(generics.CreateAPIView):
    queryset = Wards.objects.all()
    serializer_class = WardsCreateSerializers


class FeedbackListAPIView(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackListSerializers


class FeedbackCreateAPIView(generics.CreateAPIView):
    serializer_class = FeedbackCreateSerializers


class FeedbackDetailDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackCreateSerializers


class Direction_and_ServicesListAPIView(generics.ListAPIView):
    queryset = Direction_and_Services.objects.all()
    serializer_class = Direction_and_ServicesSerializers


class Direction_and_ServicesDetailAPIView(generics.RetrieveAPIView):
    queryset = Direction_and_Services.objects.all()
    serializer_class = Direction_and_ServicesDetailSerializers


class PriceListSerializersAPIView(generics.ListAPIView):
    queryset = PriceList.objects.all()
    serializer_class = PriceListSerializers


class HospitalProfileListAPIView(generics.ListAPIView):
    queryset = HospitalProfile.objects.all()
    serializer_class = HospitalProfileSerializers