from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.SimpleRouter()
# router.register(r'wards', WardsViewSet, basename='wards')


urlpatterns = [
    path('', include(router.urls)),
    path('appointment_list/', AppointmentListAPIView.as_view(), name='appointment_list'),
    path('appointment_list/<int:pk>/', AppointmentDetailDeleteUpdateAPIView.as_view(), name='appointment_delete_update'),
    path('appointment_create/', AppointmentCreateAPIView.as_view(), name='appointment_create'),

    path('medical_record_list/', MedicalRecordListAPIView.as_view(), name='medical_record_list'),
    path('medical_record_list/<int:pk>/', MedicalRecordDetailDeleteUpdateAPIView.as_view(), name='medical_record_delete_update'),
    path('medical_record_create/', MedicalRecordCreateAPIView.as_view(), name='medical_record_create'),

    path('prescription_list/', PrescriptionListAPIView.as_view(), name='prescription_list'),
    path('prescription_list/<int:pk>/', PrescriptionDetailUpdateDeleteAPIView.as_view(), name='prescription_delete_update'),
    path('prescription_create/', PrescriptionCreateAPIView.as_view(), name='prescription_list'),

    path('billings_create_list/', BillingsListCreateAPIView.as_view(), name='billings_create_list'),
    path('billings_create_list/<int:pk>/', BillingsDetailDeleteCreateAPIView.as_view(), name='billings_detail'),

    path('feedback/', FeedbackListAPIView.as_view(), name='feedback'),
    path('feedback/<int:pk>/', FeedbackDetailDeleteUpdateAPIView.as_view(), name='feedback_delete'),
    path('feedback_create/', FeedbackCreateAPIView.as_view(), name='feedback_create'),

    path('departments/', DepartmentListAPIView.as_view(), name='departments'),

    path('wards_list/', WardsListAPIView.as_view(), name='departments'),
    path('wards_create/', WardsCreateAPIView.as_view(), name='departments'),

    path('directions/', Direction_and_ServicesListAPIView.as_view(), name='directions'),
    path('directions/<int:pk>/', Direction_and_ServicesDetailAPIView.as_view(), name='directions_detail'),

    path('price_list/', PriceListSerializersAPIView.as_view(), name='price_list'),

    path('hospital_profile/', HospitalProfileListAPIView.as_view(), name='hospital_profile'),

]