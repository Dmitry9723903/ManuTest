from django.shortcuts import render


def stock(request, year):
    data = {"title": "О приложении!", "content": ""}

    return render(request, "menu/categories_by_slug.html", context=data)
