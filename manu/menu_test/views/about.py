from django.shortcuts import render


def about(request):
    data = {"title": "О приложении!", "content": ""}

    return render(request, "menu/about.html", context=data)
