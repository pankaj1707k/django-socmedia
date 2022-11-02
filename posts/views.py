from django.views import generic

from posts.models import Post


class PostListView(generic.ListView):
    template_name = "posts/feed.html"
    queryset = Post.objects.all()
    context_object_name = "posts"
    ordering = ["-updated_on"]
