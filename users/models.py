from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """A custom user model with email field required and unique"""

    email = models.EmailField(_("email"), unique=True)
