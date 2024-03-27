from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import LaundryService


User = get_user_model()

class CustomerSerializer(serializers.ModelSerializer):
    """Customer serializer."""

    class Meta:
        """Meta class for CustomerSerializer."""

        model = User
        fields=["username","email","password"]
    
    def create(self, validated_data):
        """Create a new user."""
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user
       
        
class LaundryServiceSerializer(serializers.ModelSerializer):
    dry_cleaning = serializers.BooleanField(required=False)
    dry_cleaning_and_ironing = serializers.BooleanField(required=False)
    house_cleaning = serializers.BooleanField(required=False)
    shoe_laundry = serializers.BooleanField(required=False)

    class Meta:
        model = LaundryService
        fields = ['id', 'dry_cleaning', 'dry_cleaning_and_ironing', 'house_cleaning', 'shoe_laundry']

    def create(self, validated_data):
        return LaundryService.objects.create(**validated_data)