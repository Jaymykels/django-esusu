from .api import GroupApi, GroupUsersApi, AddGroupUser
from django.urls import path

urlpatterns = [
    path("groups", GroupApi.as_view()),
    path("group/users/<int:pk>", GroupUsersApi.as_view()),
    path("add/group/user/<int:pk>", AddGroupUser.as_view())
]