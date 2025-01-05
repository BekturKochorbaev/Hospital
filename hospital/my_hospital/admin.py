from django.contrib import admin
from .models import Departments, Wards, Billings, Prescription, Feedback, MedicalRecord, Appointment, \
    Direction_and_Services, Name_Direction_and_Services, PriceList, ProcedureName, Contact, HospitalProfile

admin.site.register(Departments)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)
admin.site.register(Feedback)
admin.site.register(Prescription)
admin.site.register(Billings)
admin.site.register(Wards)


class Name_Direction_and_Services(admin.TabularInline):
    model = Name_Direction_and_Services
    extra = 1


class Direction_and_ServicesAdmin(admin.ModelAdmin):
    inlines = [Name_Direction_and_Services]


admin.site.register(Direction_and_Services, Direction_and_ServicesAdmin)


class ProcedureNameInline(admin.TabularInline):
    model = ProcedureName
    extra = 1


class PriceListAdmin(admin.ModelAdmin):
    inlines = [ProcedureNameInline]


admin.site.register(PriceList, PriceListAdmin)


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1


class HospitalProfileAdmin(admin.ModelAdmin):
    inlines = [ContactInline]


admin.site.register(HospitalProfile, HospitalProfileAdmin)