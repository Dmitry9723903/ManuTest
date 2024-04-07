from django.shortcuts import render


def categories_by_slug(request, cat_slug):
    data = {"title": "О приложении!", "content": ""}

    return render(request, "menu/categories_by_slug.html", context=data)
