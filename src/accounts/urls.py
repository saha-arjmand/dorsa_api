from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_token

urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='register'),
    path('api-token-auth/', auth_token.obtain_auth_token),
]
