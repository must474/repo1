from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate 

class Loginserializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
    
    def validate(self, data):
        if data["username"]:
           if not User.objects.filter(username=data["username"].lower()).exists():
                 raise serializers.ValidationError("Username not found")
        return data
    
    def get_tokens_for_user(self,data):
        user=authenticate(username=data["username"],password=data["password"])
        if not user:
             raise ({"message":"invalid credentials"})
        refresh = RefreshToken.for_user(user)

        return {
            'messsage':"Login success",
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }