from django.urls import path
from .views import BlogV,PublicBlogs
urlpatterns = [
    path('',BlogV.as_view()),
    path('Public/',PublicBlogs.as_view())
]