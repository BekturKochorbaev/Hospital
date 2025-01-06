from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.postgres.fields import ArrayField
from rest_framework.exceptions import ValidationError

GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('OTHER', 'OTHER'),
    )


SPECIALTIES = (
        ('cardiologist', 'Кардиолог'),
        ('dentist', 'Стоматолог'),
        ('neurologist', 'Невролог'),
        ('pediatrician', 'Педиатр'),
        ('surgeon', 'Хирург'),
        ('psychiatrist', 'Психиатр'),
        ('dermatologist', 'Дерматолог'),
        ('oncologist', 'Онколог'),
        ('gynecologist', 'Гинеколог'),
        ('urologist', 'Уролог'),
        ('orthopedist', 'Ортопед'),
        ('ophthalmologist', 'Офтальмолог'),
        ('endocrinologist', 'Эндокринолог'),
        ('immunologist', 'Иммунолог'),
        ('hematologist', 'Гематолог'),
        ('anesthesiologist', 'Анестезиолог'),
        ('radiologist', 'Рентгенолог'),
        ('pulmonologist', 'Пульмонолог'),
        ('gastroenterologist', 'Гастроэнтеролог'),
        ('rheumatologist', 'Ревматолог'),
        ('nephrologist', 'Нефролог'),
        ('nurse', 'Медсестра'),
        ('paramedic', 'Фельдшер'),
        ('general_practitioner', 'Врач общей практики'),
)


HOSPITAL_DEPARTMENTS = [
        ('emergency', 'Приемное отделение'),
        ('cardiology', 'Кардиология'),
        ('neurology', 'Неврология'),
        ('surgery', 'Хирургия'),
        ('pediatrics', 'Педиатрия'),
        ('oncology', 'Онкология'),
        ('gynecology', 'Гинекология'),
        ('urology', 'Урология'),
        ('orthopedics', 'Ортопедия'),
        ('dermatology', 'Дерматология'),
        ('radiology', 'Радиология'),
        ('anesthesiology', 'Анестезиология'),
        ('gastroenterology', 'Гастроэнтерология'),
        ('pulmonology', 'Пульмонология'),
        ('hematology', 'Гематология'),
        ('psychiatry', 'Психиатрия'),
        ('rehabilitation', 'Реабилитация'),
    ]


WORK_DAYS = [
        ('monday', 'Понедельник'),
        ('tuesday', 'Вторник'),
        ('wednesday', 'Среда'),
        ('thursday', 'Четверг'),
        ('friday', 'Пятница'),
        ('saturday', 'Суббота'),
        ('sunday', 'Воскресенье'),
    ]


class Profile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')
    profile_picture = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER)


class DoctorProfile(Profile):
    specialty = models.CharField(max_length=30, choices=SPECIALTIES)
    department = models.CharField(max_length=30, choices=HOSPITAL_DEPARTMENTS)
    shift_start = models.TimeField(null=True, blank=True)
    shift_end = models.TimeField(null=True, blank=True)
    working_days = MultiSelectField(choices=WORK_DAYS, max_choices=3)
    role = models.CharField(max_length=15, choices=[('doctor', 'doctor')], default='doctor')
    price = models.PositiveIntegerField(default=200)
    experience_year = models.PositiveIntegerField(default=1)
    qualification = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors_Profile"

    def __str__(self):
        return f'{self.first_name}-{self.last_name}-{self.specialty}'


class PatientProfile(Profile):
    BLOOD_TYPES = [
        ('A+', 'Группа крови A (положительная)'),
        ('A-', 'Группа крови A (отрицательная)'),
        ('B+', 'Группа крови B (положительная)'),
        ('B-', 'Группа крови B (отрицательная)'),
        ('AB+', 'Группа крови AB (положительная)'),
        ('AB-', 'Группа крови AB (отрицательная)'),
        ('O+', 'Группа крови O (положительная)'),
        ('O-', 'Группа крови O (отрицательная)'),
    ]
    blood_type = models.CharField(max_length=50, choices=BLOOD_TYPES)
    date_of_birth = models.DateField()
    role = models.CharField(max_length=15, choices=[('patient', 'patient')], default='patient')
    allergies = models.TextField()
    medical_history = models.TextField()

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients_Profile"

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'
