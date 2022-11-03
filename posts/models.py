from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from posts.utils import get_post_image_path

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(_("image"), upload_to=get_post_image_path)
    created_on = models.DateTimeField(_("created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("updated on"), auto_now=True)

    class Meta:
        ordering = ["-updated_on"]

    def __str__(self) -> str:
        return f"{self.id}__{self.author.username}"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(_("content"))
    created_on = models.DateTimeField(_("created_on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("updated_on"), auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self) -> str:
        return f"{self.post.id}__{self.author}"
