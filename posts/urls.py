from django.urls import path

from posts import views

urlpatterns = [
    path("feed/", views.PostListView.as_view(), name="feed"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("<int:pk>/update/", views.PostUpdateView.as_view(), name="post-update"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),
]
