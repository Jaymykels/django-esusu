from .api import GroupApi, UserGroupApi
from django.urls import path

urlpatterns = [
    path("groups", GroupApi.as_view()),
    path("group/users/<int:pk>", UserGroupApi.as_view())
]