from rest_framework import serializers
from django.contrib.auth.models import User
import re  


class Registerserializer(serializers.Serializer):
    
    username=serializers.CharField()
    email=serializers.EmailField()
    password=serializers.CharField()
    
    
    def validate(self, data):
        if data["username"]:
           if User.objects.filter(username=data["username"].lower()).exists():
                raise serializers.ValidationError({"username":"Username had been taken"})
            
        if data["email"]:
           if User.objects.filter(email=data["email"]).exists():
               raise serializers.ValidationError({"email":"email had been taken"})
           
        if data["password"]:
                password=data["password"]
                if len(password) < 8:  
                    raise serializers.ValidationError({"password":"Password should contain at least 8 characters"})
                if not re.search("[a-z]", password):  
                    raise serializers.ValidationError({"password":"Password should contain lower letters "}) 
                if not re.search("[A-Z]", password):  
                    raise serializers.ValidationError({"password":"Password should contain upper letters "})  
                if not re.search("[0-9]", password):  
                    raise serializers.ValidationError({"password":"Password should contain numbers"}) 
        return data
    
    
    def create(self, validated_data):
        user=User.objects.create(username=validated_data["username"].lower(),email=validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()
        
        return validated_data