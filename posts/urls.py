from django.urls import path

from posts import views

urlpatterns = [
    # posts
    path("feed/", views.PostListView.as_view(), name="feed"),
    path("add/", views.PostCreateView.as_view(), name="post-add"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("<int:pk>/update/", views.PostUpdateView.as_view(), name="post-update"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),
    # comments
    path("comments/add/", views.CommentCreateView.as_view(), name="comment-add"),
    path(
        "comments/<int:pk>/update/",
        views.CommentUpdateView.as_view(),
        name="comment-update",
    ),
    path(
        "comments/<int:pk>/delete/",
        views.CommentDeleteView.as_view(),
        name="comment-delete",
    ),
    # like
    path("like/", views.LikeToggleView.as_view(), name="like-post"),
]
