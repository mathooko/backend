from rest_framework import generics
from .serializers import CustomerSerializer
from django.contrib.auth import get_user_model,authenticate
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.response import Response
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
            return Response({"access_token": str(access_token)})
        else:
            # User authentication failed
            return Response({"error": "Invalid credentials"}, status=401)

class LaundryServiceView(generics.ListCreateAPIView):
    queryset = LaundryService.objects.all()
    serializer_class = LaundryServiceSerializer

class SelectedView(generics.RetrieveAPIView):
    queryset = LaundryService.objects.all()
    serializer_class = LaundryServiceSerializer