from django.db import models

class Department(models.Model):
    DepartmentName = models.CharField(max_length=50)
    DepartmentID = models.CharField(max_length=15)

    def __str__(self):
        return self.DepartmentName

class Doctor(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,unique=True)
    PhoneNumber = models.IntegerField()
    StaffID = models.CharField(max_length=15,unique=True)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.FirstName
