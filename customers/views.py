from rest_framework import generics
from .serializers import CustomerSerializer
from django.contrib.auth import get_user_model
user = get_user_model()

class CustomerListView(generics.ListCreateAPIView):
    queryset=user.objects.all()
    serializer_class=CustomerSerializer
    