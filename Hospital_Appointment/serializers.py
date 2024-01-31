from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Doctor, Department, Patient, Appointments


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ("DepartmentName", "DepartmentID")


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password")


class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = "__all__"
