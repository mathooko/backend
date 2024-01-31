from rest_framework import generics
from django.contrib.auth.models import User

from .serializers import (
    DepartmentSerializer,
    DoctorSerializer,
    UserSerializer,
    PatientSerializer,
    AppointmentsSerializer,
)
from .models import Department, Doctor, Patient, Appointments


class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DoctorDetails(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class PatientDetails(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class UserRegistration(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AppointmentsDetails(generics.ListCreateAPIView):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentsSerializer
