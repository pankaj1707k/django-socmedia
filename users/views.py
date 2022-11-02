from django.shortcuts import render


def home_view(request):
    if request.user.is_authenticated:
        return render(request, "feed.html")
    return render(request, "home.html")
