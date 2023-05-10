from django.urls import path,include
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('account/',include('app1.urls')),
    path('blog/',include("home.urls"))
]