from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views import generic

from users import forms


def home_view(request):
    if request.user.is_authenticated:
        return render(request, "feed.html")
    return render(request, "home.html")


class RegisterView(generic.TemplateView):
    template_name = "register.html"
    form_class = forms.UserRegisterForm

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["title"] = "SocMed | Register"
        return context

    def get(self, request):
        form = self.form_class()
        context = self.get_context_data()
        context["form"] = form
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect("home")
        context = self.get_context_data()
        context["form"] = form
        return render(request, self.template_name, context)


class LoginView(generic.TemplateView):
    template_name = "login.html"
    form_class = forms.UserLoginForm

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["title"] = "SocMed | Register"
        return context

    def get(self, request):
        form = self.form_class()
        context = self.get_context_data()
        context["form"] = form
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "Logged in!")
                return redirect("home")
            else:
                messages.error(request, "Invalid credentials")
        context = self.get_context_data()
        context["form"] = form
        return render(request, self.template_name, context)
