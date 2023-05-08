from rest_framework.views import APIView
from ..serializers.Login import Loginserializer
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

class Login(APIView):
    def post(self, request):
            data = request.data
            serializer = Loginserializer(data=data)
            if not serializer.is_valid():
                raise ValidationError(serializer.errors)
                           
            response = serializer.get_tokens_for_user(serializer.data)
                       
            access_token = response['access']
            response_obj = HttpResponse()
            response_obj.set_cookie('access_token', access_token, httponly=True)
    
            refresh_token = response['refresh']
            response_obj.set_cookie('refresh_token', refresh_token, httponly=True)

            return response_obj