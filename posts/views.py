from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic

from posts.forms import CommentForm, PostForm
from posts.models import Comment, Post


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
    context_object_name = "post"


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
