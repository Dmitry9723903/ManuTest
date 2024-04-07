from django.shortcuts import render


def home(request):
    data = {"title": "Привет!", "content": ""}

    return render(request, "index.html", context=data)
