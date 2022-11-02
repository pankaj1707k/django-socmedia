from django.urls import path

from posts import views

urlpatterns = [
    path("feed/", views.PostListView.as_view(), name="feed"),
]
