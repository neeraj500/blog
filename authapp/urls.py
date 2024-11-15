from django.urls import path, include
from .views import authView, home

urlpatterns = [
    path("login/", home, name="login"),
    path("signup/", authView, name="signup"),
    path("accounts/", include("django.contrib.auth.urls"))
]
