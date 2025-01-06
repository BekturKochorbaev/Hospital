from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

from .permissions import CheckDoctor, CheckPatient, CheсkReview
from .serializers import *
from profile_app.models import *
from rest_framework import viewsets, generics
from rest_framework import permissions

class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class DepartmentListAPIView(generics.ListAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializers


class AppointmentListAPIView(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentListSerializers


class AppointmentCreateAPIView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentCreateSerializers
    permission_classes = [CheckPatient]


class AppointmentDetailDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentListSerializers
    permission_classes = [CheckPatient]


class MedicalRecordListAPIView(generics.ListAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordListSerializers


class MedicalRecordCreateAPIView(generics.CreateAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordCreateSerializers
    permission_classes = [CheckDoctor]


class MedicalRecordDetailDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordListSerializers
    permission_classes = [CheckDoctor]


class PrescriptionListAPIView(generics.ListAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionListSerializers


class PrescriptionDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionListSerializers
    permission_classes = [CheckDoctor]


class PrescriptionCreateAPIView(generics.CreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionListSerializers
    permission_classes = [CheckDoctor]


class BillingsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Billings.objects.all()
    serializer_class = BillingsListCreateSerializers
    permission_classes = [CheckDoctor]


class BillingsDetailDeleteCreateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Billings.objects.all()
    serializer_class = BillingsListCreateSerializers
    permission_classes = [CheckDoctor]


class WardsListAPIView(generics.ListAPIView):
    queryset = Wards.objects.all()
    serializer_class = WardsListSerializers


class WardsCreateAPIView(generics.CreateAPIView):
    queryset = Wards.objects.all()
    serializer_class = WardsCreateSerializers
    permission_classes = [CheckDoctor]


# class FeedbackListAPIView(generics.ListAPIView):
#     queryset = Feedback.objects.all()
#     serializer_class = FeedbackListSerializers


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializers
    permission_classes = [permissions.IsAuthenticated, CheсkReview]


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


class DoctorProfileListAPIView(generics.ListAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSimpleSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['department', 'specialty', 'price', 'working_days']
    ordering_fields = ['price']
    pagination_class = Pagination

    # def get_queryset(self):
    #     return DoctorProfile.objects.filter(id=self.request.user.id)
