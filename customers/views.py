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

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        services = []
        for field_name in ['dry_cleaning', 'dry_cleaning_and_ironing', 'house_cleaning', 'shoe_laundry']:
            if field_name in data:
                if data[field_name]:
                    services.append(field_name.replace('_', ' '))
                del data[field_name]
        data['service'] = ', '.join(services)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
