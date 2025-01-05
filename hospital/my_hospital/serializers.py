from rest_framework import serializers
from .models import *
from profile_app.models import *
from profile_app.serializers import *


class PatientProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = ['first_name', 'last_name']


class DoctorProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = ['first_name', 'last_name', 'specialty', 'experience_year', 'profile_picture']


class DepartmentsSerializers(serializers.ModelSerializer):
    chief_physician = serializers.SerializerMethodField()

    class Meta:
        model = Departments
        fields = '__all__'

    def get_chief_physician(self, obj):
        return f"{obj.chief_physician.first_name} {obj.chief_physician  .last_name}"

# class DepartmentsSerializers(serializers.ModelSerializer):
#     chief_physician = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Departments
#         fields = '__all__'


class AppointmentListSerializers(serializers.ModelSerializer):
    date_time = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    doctor = serializers.SerializerMethodField()
    patient = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = '__all__'

    def get_patient(self, obj):
        return f"{obj.patient.first_name} {obj.patient.last_name}"

    def get_doctor(self, obj):
        return f"{obj.doctor.first_name} {obj.doctor.last_name}"


class AppointmentCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['patient', 'doctor', 'status', 'notes', 'date_time']


class MedicalRecordListSerializers(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    doctor = serializers.SerializerMethodField()
    patient = serializers.SerializerMethodField()

    class Meta:
        model = MedicalRecord
        fields = '__all__'

    def get_patient(self, obj):
        return f"{obj.patient.first_name} {obj.patient.last_name}"

    def get_doctor(self, obj):
        return f"{obj.doctor.first_name} {obj.doctor.last_name}"


class MedicalRecordCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = ['patient', 'doctor', 'diagnosis', 'treatment', 'prescribed_medication']


class PrescriptionListSerializers(serializers.ModelSerializer):
    doctor = serializers.SerializerMethodField()
    patient = serializers.SerializerMethodField()

    class Meta:
        model = Prescription
        fields = "__all__"
    def get_patient(self, obj):
        return f"{obj.patient.first_name} {obj.patient.last_name}"

    def get_doctor(self, obj):
        return f"{obj.doctor.first_name} {obj.doctor.last_name}"



class PrescriptionCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = "__all__"

class BillingsListCreateSerializers(serializers.ModelSerializer):
    date = serializers.DateTimeField('%d-%m-%Y %H-%M')
    patients = serializers.SerializerMethodField()

    class Meta:
        model = Billings
        fields = '__all__'


class WardsListSerializers(serializers.ModelSerializer):
    patients = PatientProfileSimpleSerializers(read_only=True, many=True)
    count_patient = serializers.SerializerMethodField()
    total_capacity = serializers.SerializerMethodField()
    class Meta:
        model = Wards
        fields = '__all__'

    def get_count_patient(self, obj):
        return obj.get_count_patient()

    def get_total_capacity(self, obj):
        return obj.get_total_capacity()


class WardsCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Wards
        fields = '__all__'



class FeedbackListSerializers(serializers.ModelSerializer):
    patient = serializers.SerializerMethodField()
    doctor = serializers.SerializerMethodField()

    class Meta:
        model = Feedback
        fields = ['patient', 'rating', 'doctor', 'comment']

    def get_patient(self, obj):
        return f"{obj.patient.first_name} {obj.patient.last_name}"

    def get_doctor(self, obj):
        return f"{obj.doctor.first_name} {obj.doctor.last_name}"


class FeedbackCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class Name_Direction_and_ServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Name_Direction_and_Services
        fields = ['description']


class Direction_and_ServicesSerializers(serializers.ModelSerializer):
    service_name = Name_Direction_and_ServicesSerializers(read_only=True, many=True)

    class Meta:
        model = Direction_and_Services
        fields = ['name', 'picture', 'service_name']


class Direction_and_ServicesDetailSerializers(serializers.ModelSerializer):
    doctor = DoctorProfileSimpleSerializers(read_only=True, many=True)

    class Meta:
        model = Direction_and_Services
        fields = ['name', 'description', 'doctor']


class ProcedureNameSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProcedureName
        fields = ['procedure', 'price']


class PriceListSerializers(serializers.ModelSerializer):
    procedure_name = ProcedureNameSerializers(read_only=True , many=True)

    class Meta:
        model = PriceList
        fields = ['name', 'procedure_name']


class PriceListDetailSerializers(serializers.ModelSerializer):
    procedure_name = ProcedureNameSerializers(read_only=True)

    class Meta:
        model = PriceList
        fields = ['name', 'procedure_name']


class HospitalProfileSerializers(serializers.ModelSerializer):
    chief_physician = DoctorProfileSimpleSerializers(read_only=True)
    count_doctor = serializers.SerializerMethodField()
    count_patient = serializers.SerializerMethodField()
    count_consultation = serializers.SerializerMethodField()

    class Meta:
        model = HospitalProfile
        fields = ['hospital_name', 'hospital_image', 'description', 'chief_physician', 'operating_mode',
                  'count_doctor', 'count_patient', 'count_consultation']

    def get_count_doctor(self, obj):
        return obj.get_count_doctor()

    def get_count_patient(self, obj):
        return obj.get_count_patient()

    def get_count_consultation(self, obj):
        return obj.get_count_consultation()
