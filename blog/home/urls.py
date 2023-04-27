from django.urls import path
from .views.Blog import BlogV
from .views.PublicBlog import PublicBlogs

urlpatterns = [
    path('',BlogV.as_view()),
    path('Public/',PublicBlogs.as_view())
]