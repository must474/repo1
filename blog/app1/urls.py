from django.urls import path
from .views.Login import Login
from .views.Register import Register
from .views.Logout import Logout
urlpatterns = [
    path('register/',Register.as_view()),
    path('login/',Login.as_view()),
    path('logout/',Logout.as_view())
]