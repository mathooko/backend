from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import LaundryService


User = get_user_model()

class CustomerSerializer(serializers.ModelSerializer):
    """Customer serializer."""

    class Meta:
        """Meta class for CustomerSerializer."""

        model = User
        fields=["id","username","email","password"]
    
    def create(self, validated_data):
        """Create a new user."""
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user
       
        
class LaundryServiceSerializer(serializers.ModelSerializer):
        class Meta:
             model = LaundryService 
             fields = "__all__"

        def to_representation(self, instance):
            data = super().to_representation(instance)
            return {key: value for key, value in data.items() if value is not None}