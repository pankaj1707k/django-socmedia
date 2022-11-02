from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm

User = get_user_model()


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")


class UserRegisterForm(BaseUserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username/Email")
    password = forms.CharField(widget=forms.PasswordInput())
