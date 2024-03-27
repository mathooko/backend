from django.db import models

class LaundryService(models.Model):
    DRY_CLEANING = 'Drycleaning'
    DRY_CLEANING_AND_IRONING = 'Drycleaning and ironing'
    HOUSE_CLEANING = 'House cleaning'
    SHOE_LAUNDRY = 'Shoe laundry'

    SERVICE_CHOICES = [
        (DRY_CLEANING, 'Drycleaning'),
        (DRY_CLEANING_AND_IRONING, 'Drycleaning and ironing'),
        (HOUSE_CLEANING, 'House cleaning'),
        (SHOE_LAUNDRY, 'Shoe laundry'),
    ]

    service = models.CharField(max_length=100, blank=True)
