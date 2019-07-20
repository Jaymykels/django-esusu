from .api import GroupApi
from django.urls import path

urlpatterns = [
    path("groups", GroupApi.as_view()),    
]