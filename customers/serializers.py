from rest_framework import serializers
from django.contrib.auth import get_user_model


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
       
        
