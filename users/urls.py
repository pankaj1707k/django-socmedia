from django.urls import path

from users import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
]
