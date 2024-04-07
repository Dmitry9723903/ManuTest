from django.shortcuts import render


def category(request, cat_id):
    data = {"title": "О приложении!", "content": ""}

    return render(request, "menu/categories.html", context=data)
