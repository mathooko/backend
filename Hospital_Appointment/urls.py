from django.urls import path

from .views import DepartmentList, DoctorDetails

urlpatterns = [
    path('department/', DepartmentList.as_view()),
    path('doctor/', DoctorDetails.as_view()),
]