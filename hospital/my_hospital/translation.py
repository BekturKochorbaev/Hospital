from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Departments)
class DepartmentsTranslationOptions(TranslationOptions):
    fields = ('name', 'location')


@register(MedicalRecord)
class MedicalRecordTranslationOptions(TranslationOptions):
    fields = ('diagnosis', 'treatment', 'prescribed_medication')


@register(Prescription)
class PrescriptionTranslationOptions(TranslationOptions):
    fields = ('medication', 'dosage')


@register(Direction_and_Services)
class Direction_and_ServicesTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Name_Direction_and_Services)
class Name_Direction_and_ServicesTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(PriceList)
class PriceListTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(ProcedureName)
class ProcedureNameTranslationOptions(TranslationOptions):
    fields = ('procedure',)


@register(HospitalProfile)
class HospitalProfileTranslationOptions(TranslationOptions):
    fields = ('hospital_name', 'address', 'description', 'operating_mode')




