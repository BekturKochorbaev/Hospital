from rest_framework import permissions

from profile_app.models import PatientProfile, DoctorProfile


class CheckDoctor(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if isinstance(user, DoctorProfile) and user.role == 'doctor':
            return True
        return False


class CheckPatient(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if isinstance(user, PatientProfile) and user.role == 'patient':
            return True
        return False


class CheсkReview(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.patient == request.user
