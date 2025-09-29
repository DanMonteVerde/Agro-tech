from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, login_view
urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", register, name="register"),
]
