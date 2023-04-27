from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import Registerserializer
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