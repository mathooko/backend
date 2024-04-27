from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class LaundryService(models.Model):
   user = models.ForeignKey(User, on_delete = models.CASCADE)
   trousers = models.IntegerField(null=True)
   tshirts = models.IntegerField(null=True)
   sweaters = models.IntegerField(null=True)
   shorts = models.IntegerField(null=True)
   personal = models.IntegerField(null=True)
   duvet = models.IntegerField(null=True)
   shoes = models.IntegerField(null=True)
   price = models.FloatField(null=True)
   
   def __str__(self):
        return f"LaundryService ID: {self.id}"