from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Blog
from django.db.models import Q
class BlogV(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    def get(self,request):
        try:
            blogs=Blog.objects.filter(user=request.user)
            search_query = request.GET.get("search", "")
            if request.GET.get("search", ""):
                search=request.GET.get("search") 
                blogs=blogs.filter(Q(title__contains=search) | Q(text__contains= search)) # icontains


            serializer=BlogSerializer(blogs,many=True)
            return Response({
                            'data':serializer.data,
                            "message":"Blogs have gotten"},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                        'data':{},
                        "message":"something went wrong"},
                        status=status.HTTP_400_BAD_REQUEST
                )
            

    def post(self,request):
        try:
            data=request.data
            data["user"]=request.user.id
            serializer=BlogSerializer(data=data)
            if not serializer.is_valid():
                return Response({
                        'data':serializer.errors,
                        "message":"something went wrong"},
                        status=status.HTTP_400_BAD_REQUEST
                )
            serializer.save()
            return Response({
                        'data':serializer.data,
                        "message":"Blog was created"},
                        status=status.HTTP_201_CREATED
                )

        except Exception as e:
            return Response({
                        'data':{},
                        "message":"something went wrong"},
                        status=status.HTTP_400_BAD_REQUEST
                )
    def patch(self,request):
        try:
            data=request.data
            
            blog=Blog.objects.filter(uid=data.get("uid"))
            if not blog.exists():
                return Response({
                            'data':serializer.errors,
                            "message":"There is no blog like that"},
                            status=status.HTTP_400_BAD_REQUEST
                    )
            if  blog[0].user!=request.user:
                return Response({
                            'data':{},
                            "message":"You are not able to change this block"},
                            status=status.HTTP_400_BAD_REQUEST
                    )
            serializer=BlogSerializer(blog[0],data=data,partial=True)
            if not serializer.is_valid():
                return Response({
                            'data':{},
                            "message":"Serializer is not valid"},
                            status=status.HTTP_400_BAD_REQUEST
                    )
            serializer.save()
            return Response({
                            'data':serializer.data,
                            "message":"Blog was updated"},
                            status=status.HTTP_200_OK
                    )
        except Exception as e:
            return Response({
                        'data':{},
                        "message":"something went wrong"},
                        status=status.HTTP_400_BAD_REQUEST
                )
        
    def delete(self,request):
        try:
            data=request.data
            blog=Blog.objects.filter(uid=data.get("uid"))
            if not blog.exists():
                    return Response({
                                    'data':{},
                                    "message":"There is no blog like that"},
                                    status=status.HTTP_400_BAD_REQUEST
                            )
            if  blog[0].user!=request.user:
                    return Response({
                                    'data':{},
                                    "message":"You are not able to change this block"},
                                    status=status.HTTP_400_BAD_REQUEST
                            )
            blog[0].delete()
            return Response({
                                    'data':{},
                                    "message":"Deleted"},
                                    status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                        'data':{},
                        "message":"something went wrong"},
                        status=status.HTTP_400_BAD_REQUEST
                )
        
class PublicBlogs(APIView):
    def get(self,request):
        try:
            blogs=Blog.objects.all().order_by("?")
            if request.GET.get("search"):
                search=request.GET.get("search") 
                blogs=blogs.filter(Q(title__contains=search) | Q(text__contains= search))

            # page_number=request.GET.get('page',1)
            # paginator=Paginator(blogs,2)
            serializer=BlogSerializer(blogs,many=True)
            return Response({
                            'data':serializer.data,
                            "message":"Blogs have gotten"},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                        'data':{},
                        "message":"something went wrong"},
                        status=status.HTTP_400_BAD_REQUEST
                )

        




        


       

