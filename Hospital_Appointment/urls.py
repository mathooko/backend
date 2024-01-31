from django.urls import path

from .views import (
    DepartmentList,
    DoctorDetails,
    UserRegistration,
    PatientDetails,
    AppointmentsDetails,
)

urlpatterns = [
    path("department/", DepartmentList.as_view()),
    path("doctor/", DoctorDetails.as_view()),
    path("user/", UserRegistration.as_view()),
    path("patient/", PatientDetails.as_view()),
    path("appointments/", AppointmentsDetails.as_view()),
]
