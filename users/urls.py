from django.urls import path
from .views import CustomUserCreateView

app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreateView.as_view(), name='create_user'),
]