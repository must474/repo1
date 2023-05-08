from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.http import Http404
from rest_framework_simplejwt.tokens import TokenError



class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception,ValidationError):
            return Response({
                'error': exception.detail,
                'message': 'Validation error occurred'
            }, status=status.HTTP_400_BAD_REQUEST)
        if isinstance(exception,PermissionError):
            return Response({
                'error': exception.detail,
                'message': 'You can not do this task'
            }, status=status.HTTP_403_FORBIDDEN)
        if isinstance(exception,Http404):
            return Response({
                'error': exception.detail,
                'message': 'Not Found'
            }, status=status.HTTP_404_NOT_FOUND)
        if isinstance(exception,TokenError):
            return Response({
                'error': exception.detail,
                'message': 'Token problem'
                
            },status=status.HTTP_400_BAD_REQUEST)
        



        return Response({
            'message': 'Server error occurred'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

       

