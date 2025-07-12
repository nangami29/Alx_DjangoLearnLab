from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(
            username= validated_data['username'],
            email= validated_data ['email'],
            password= validated_data ['password']
        )

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)


    def validate(self, attrs):
        user= authenticate(username=attrs.get('username'), email=attrs.get('email'), password=attrs.get('password'))
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        attrs['user']= user
        return attrs
