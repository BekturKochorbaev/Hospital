from django.db import models
from profile_app.models import *
from phonenumber_field.modelfields import PhoneNumberField

class Departments(models.Model):
    name = models.CharField(max_length=60, choices=HOSPITAL_DEPARTMENTS)
    location = models.CharField(max_length=250)
    chief_physician = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, verbose_name='главный врач')

    def __str__(self):
        return f'{self.location}'


class Appointment(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='patient_name')
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='doctor_name')
    date_time = models.DateTimeField()
    STATUS = (
        ('scheduled', 'scheduled'),
        ('completed', 'completed'),
        ('canceled', 'canceled')
    )
    status = models.CharField(max_length=10, choices=STATUS)
    notes = models.TextField()

    def __str__(self):
        return f'{self.patient}-{self.status}'


class MedicalRecord(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='patient')
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='doctor')
    diagnosis = models.TextField()
    treatment = models.TextField()
    prescribed_medication = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.patient}-{self.diagnosis}'


class Feedback(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='patient_review')
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='doctor_review')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.patient}-{self.rating}'


class Prescription(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='name_patient')
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='name_doctor')
    medication = models.CharField(max_length=250)
    dosage = models.CharField(max_length=350)

    def __str__(self):
        return f'{self.patient}-{self.medication}'


class Billings(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='patient_billing')
    total_amount = models.PositiveIntegerField()
    paid = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.paid}-{self.total_amount}"


class Wards(models.Model):
    name = models.CharField(max_length=100)
    WARD_TYPE =(
        ('VIP', 'VIP'),
        ('STANDARD', 'STANDARD'),
    )
    ward_type = models.CharField(max_length=12, choices=WARD_TYPE, default='STANDARD')
    capacity = models.PositiveIntegerField(default=5)
    patients = models.ManyToManyField(PatientProfile)

    def get_count_patient(self):
        patients = self.patients
        return patients.count()

    def get_total_capacity(self):
       return self.capacity-self.get_count_patient()


class Direction_and_Services(models.Model):
    name = models.CharField(max_length=250)
    picture = models.ImageField(upload_to='pictures/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    doctor = models.ManyToManyField(DoctorProfile,)

    def __str__(self):
        return self.name


class Name_Direction_and_Services(models.Model):
    name = models.ForeignKey(Direction_and_Services, on_delete=models.CASCADE, related_name='service_name')
    description = models.CharField(max_length=250)


class PriceList(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class ProcedureName(models.Model):
    procedure = models.CharField(max_length=150)
    procedure_name = models.ForeignKey(PriceList, on_delete=models.CASCADE, related_name='procedure_name')
    price = models.PositiveIntegerField()


class HospitalProfile(models.Model):
    hospital_name = models.CharField(max_length=32, unique=True)
    hospital_image = models.ImageField(upload_to='hospital_image/')
    address = models.CharField(max_length=32)
    description = models.TextField()
    chief_physician = models.OneToOneField(DoctorProfile, on_delete=models.CASCADE, verbose_name='Главный врач')
    operating_mode = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.hospital_name}, {self.chief_physician}'

    def get_count_doctor(self):
        doctor = DoctorProfile.objects.all()
        return doctor.count()

    def get_count_patient(self):
        patient = PatientProfile.objects.all()
        return patient.count()

    def get_count_consultation(self):
        patient = Appointment.objects.all()
        return patient.count()


class Contact(models.Model):
    hospital = models.ForeignKey(HospitalProfile, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)