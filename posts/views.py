from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect, render
from django.views import View, generic

from posts.forms import PostForm
from posts.models import Post


class PostListView(generic.ListView):
    template_name = "posts/feed.html"
    queryset = Post.objects.all()
    context_object_name = "posts"
    ordering = ["-updated_on"]


class PostDetailView(generic.DetailView):
    template_name = "posts/post_detail.html"
    model = Post
    context_object_name = "post"


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    template_name = "posts/post_form.html"
    form_class = PostForm
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
