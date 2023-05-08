from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.Blog import BlogSerializer
from ..models import Blog
from django.db.models import Q


class PublicBlogs(APIView):
    def get(self,request):
           
            blogs=Blog.objects.all().order_by("?")
            if request.GET.get("search"):
                search=request.GET.get("search") 
                blogs=blogs.filter(Q(title__icontains=search) | Q(text__iontains= search))

            # page_number=request.GET.get('page',1)
            # paginator=Paginator(blogs,2)
            serializer=BlogSerializer(blogs,many=True)
            
            return Response({
                            'data':serializer.data,
                            "message":"Blogs have gotten"},
                            status=status.HTTP_200_OK)
            