from django.urls import path
from .api import (
    RegisterApi,
    LoginApi
)
from knox import views as knox_views


urlpatterns = [
    path("register", RegisterApi.as_view()),
    path("login", LoginApi.as_view()),
    path("logout", knox_views.LogoutView.as_view(), name="knox_logout"),
]
