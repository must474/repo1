from django.urls import path,include
urlpatterns = [
    path('account/',include('app1.urls')),
    path('blog/',include("home.urls"))
]