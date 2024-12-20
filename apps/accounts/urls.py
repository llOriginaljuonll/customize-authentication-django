from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = "accounts"

urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", views.CustomUserCreationView.as_view(), name="signup"),
]
