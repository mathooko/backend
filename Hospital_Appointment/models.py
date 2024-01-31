from django.db import models


class Department(models.Model):
    DepartmentName = models.CharField(max_length=50)
    DepartmentID = models.CharField(max_length=15)

    def __str__(self):
        return self.DepartmentName


class Doctor(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    PhoneNumber = models.IntegerField()
    Doctor_StaffID = models.CharField(max_length=15, unique=True)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.Doctor_StaffID


class Patient(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    PhoneNumber = models.IntegerField()
    Patient_IDNumber = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.Patient_IDNumber


class Appointments(models.Model):
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    AppointmentDate = models.DateField()
    AppointmentTime = models.TimeField()

    def __str__(self):
        return (
            str(self.Patient)
            + " "
            + str(self.Doctor)
            + " "
            + str(self.AppointmentDate)
            + " "
            + str(self.AppointmentTime)
        )
