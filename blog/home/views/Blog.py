from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.Blog import BlogSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..models import Blog
from django.db.models import Q
from rest_framework.exceptions import ValidationError
from django.http import Http404


class BlogV(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    def get(self,request):
            blogs=Blog.objects.filter(user=request.user)
            if request.GET.get("search"):
                search=request.GET.get("search") 
                blogs=blogs.filter(Q(title__icontains=search) | Q(text__icontains= search)) # icontains


            serializer=BlogSerializer(blogs,many=True)
            return Response({
                            'data':serializer.data,
                            "message":"Blogs have gotten"},
                            status=status.HTTP_200_OK)
            

    def post(self,request):
            data=request.data
            data["user"]=request.user.id
            serializer=BlogSerializer(data=data)
            
            if not serializer.is_valid():
                    raise ValidationError(serializer.errors)
                   
            serializer.save()
            return Response({
                        'data':serializer.data,
                        "message":"Blog was created"},
                        status=status.HTTP_201_CREATED
                )

            
    def patch(self,request):
            data=request.data
            blog=Blog.objects.filter(uid=data.get("uid"))
            
            if blog.exists() and blog[0].user==request.user:
                serializer=BlogSerializer(blog[0],data=data,partial=True)
                if not serializer.is_valid():
                        raise ValidationError(serializer.errors)

                serializer.save()
                return Response({
                                'data':serializer.data,
                                "message":"Blog was updated"},
                                status=status.HTTP_200_OK)
                
        
    def delete(self,request):
            data=request.data
            blog=Blog.objects.filter(uid=data.get("uid"))
            if not blog.exists():
                    raise Http404("There is no blog like that")
                    
            if  blog[0].user!=request.user:
                    raise PermissionError("You can not delete this blog")

            blog[0].delete()
            return Response({
                                    'data':{},
                                    "message":"Deleted"},
                                    status=status.HTTP_204_NO_CONTENT)

        