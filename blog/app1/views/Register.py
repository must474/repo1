from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.Register import Registerserializer
from rest_framework.exceptions import ValidationError
class Register(APIView):
    def post(self,request):

            data=request.data
            serializer=Registerserializer(data=data)
            if not serializer.is_valid():
                    raise ValidationError(serializer.errors)
            serializer.save()
            return Response({
                        'data':{},
                        "message":"your account was created"},
                        status=status.HTTP_201_CREATED)
                
                
