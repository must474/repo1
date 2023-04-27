from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Registerserializer,Loginserializer

class Register(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=Registerserializer(data=data)
            if not serializer.is_valid():
                
                return Response({
                        'data':serializer.errors,
                        "message":"something went wrong"},
                        status=status.HTTP_400_BAD_REQUEST
                )
            serializer.save()
            
            return Response({
                        'data':{},
                        "message":"your account was created"},
                        status=status.HTTP_201_CREATED
                )
                
        except Exception as e:
             return Response({
                        'data':{},
                        "message":"something went wrong"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
from django.http import HttpResponse
from rest_framework.views import APIView

class Login(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = Loginserializer(data=data)
            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    "message": "something went wrong"
                }, status=status.HTTP_400_BAD_REQUEST)
            
            response = serializer.get_tokens_for_user(serializer.data)
            
            
            access_token = response['access']
            response_obj = HttpResponse()
            response_obj.set_cookie('access_token', access_token, httponly=True)
    
            refresh_token = response['refresh']
            response_obj.set_cookie('refresh_token', refresh_token, httponly=True)
            

            return response_obj
            
        except Exception as e:
            return Response({
                'data': {},
                "message": "something went wrong"
            }, status=status.HTTP_400_BAD_REQUEST)




             
