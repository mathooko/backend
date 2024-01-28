from django.shortcuts import render
from rest_framework import generics
from .serializers import DepartmentSerializer,DoctorSerializer
from .models import Department,Appointment, Doctor, User


class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
class DoctorDetails(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer