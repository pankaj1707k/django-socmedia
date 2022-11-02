from django.urls import path

from posts import views

urlpatterns = [
    path("feed/", views.PostListView.as_view(), name="feed"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
]
