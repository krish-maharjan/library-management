from django.urls import path
from .views import ValidateTokenAPI

urlpatterns = [
    # your other url patterns
    path('user', ValidateTokenAPI.as_view(), name='validate_token'),
]
