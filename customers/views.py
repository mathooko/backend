from rest_framework import generics
from .serializers import CustomerSerializer
from django.contrib.auth import get_user_model,authenticate
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.response import Response
from rest_framework import status
from .models import LaundryService
from .serializers import LaundryServiceSerializer

user = get_user_model()


class CustomerListView(generics.ListCreateAPIView):
    queryset=user.objects.all()
    serializer_class=CustomerSerializer
class CustomerLoginView(generics.ListCreateAPIView):
    """View for user login."""

    def post(self, request):
        """Handle user login."""
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user is not None:
            # User authentication successful, generate JWT token
            access_token = AccessToken.for_user(user)
            return Response({"access_token": str(access_token),"user_id": user.id,
                    "username": user.username,})
        else:
            # User authentication failed
            return Response({"error": "Invalid credentials"}, status=401)

class LaundryServiceView(generics.ListCreateAPIView):
    queryset = LaundryService.objects.all()
    serializer_class = LaundryServiceSerializer
   

class SelectedView(generics.RetrieveAPIView):
    
    serializer_class = LaundryServiceSerializer

    def get(self, request, *args, **kwargs):
        order = LaundryService.objects.filter(user=kwargs["user"])
        serialized_orders = LaundryServiceSerializer(order, many=True)
        return Response(serialized_orders.data, status=200)

class OrderEdit(generics.RetrieveUpdateDestroyAPIView):
    """View for editing an Order."""

    serializer_class = LaundryServiceSerializer

    def get_queryset(self):
        queryset = LaundryService.objects.filter(id=self.kwargs["pk"])
        return queryset

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response()