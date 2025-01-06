from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin

from .models import Departments, Wards, Billings, Prescription, Feedback, MedicalRecord, Appointment, \
    Direction_and_Services, Name_Direction_and_Services, PriceList, ProcedureName, Contact, HospitalProfile

@admin.register(Departments)
class DepartmentsAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(MedicalRecord)
class MedicalRecordAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Prescription)
class PrescriptionAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(Appointment)
admin.site.register(Feedback)
admin.site.register(Billings)
admin.site.register(Wards)


class Name_Direction_and_Services(TranslationInlineModelAdmin, admin.TabularInline):
    model = Name_Direction_and_Services
    extra = 1


@admin.register(Direction_and_Services)
class Direction_and_ServicesAdmin(TranslationAdmin):
    inlines = [Name_Direction_and_Services]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class ProcedureNameInline(TranslationInlineModelAdmin, admin.TabularInline):
    model = ProcedureName
    extra = 1


@admin.register(PriceList)
class PriceListAdmin(TranslationAdmin):
    inlines = [ProcedureNameInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1


@admin.register(HospitalProfile)
class HospitalProfileAdmin(TranslationAdmin):
    inlines = [ContactInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }