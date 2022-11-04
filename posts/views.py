from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View, generic

from posts.forms import CommentForm, PostForm
from posts.models import Comment, Like, Post


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = "posts/post_form.html"
    form_class = PostForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostListView(generic.ListView):
    template_name = "posts/feed.html"
    queryset = Post.objects.all()
    context_object_name = "posts"
    ordering = ["-updated_on"]


class PostDetailView(generic.DetailView):
    template_name = "posts/post_detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        context["comments"] = Comment.objects.all().order_by("-created_on")
        return context


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    template_name = "posts/post_form.html"
    form_class = PostForm
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    success_url = "/"
    context_object_name = "post"
    template_name = "posts/post_confirm_delete.html"

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    template_name = "posts/comment_form.html"
    form_class = CommentForm

    def get_success_url(self) -> str:
        return f"/posts/{self.request.GET.get('ppk')}/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(pk=self.request.GET.get("ppk"))
        return super().form_valid(form)


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Comment
    template_name = "posts/comment_form.html"
    form_class = CommentForm

    def get_success_url(self) -> str:
        comment = self.get_object()
        return f"/posts/{comment.post.id}/"

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Comment
    template_name = "posts/comment_confirm_delete.html"

    def get_success_url(self) -> str:
        comment = self.get_object()
        return f"/posts/{comment.post.id}/"

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user


class LikeToggleView(LoginRequiredMixin, View):
    model = Like

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.request.GET.get("ppk"))
        try:
            like = self.model.objects.get(post=post, author=self.request.user)
            like.delete()
        except self.model.DoesNotExist:
            like = self.model.objects.create(post=post, author=self.request.user)
            like.save()
        return redirect("post-detail", pk=post.id)
