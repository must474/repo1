from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from ..serializers.Logout import LogoutS

class Logout(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    
    def post(self,request):
        serializer=LogoutS(data=request.data)
        if serializer.is_valid():
            serializer.save()

            
        

        return Response(status=status.HTTP_200_OK)
        