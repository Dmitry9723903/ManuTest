from django.conf import settings
from django.urls import path, register_converter
from . import convertors
from .views import (
    home,
    about,
    category,
    categories_by_slug,
    stock,
    error_403,
    error_404,
    error_500,
)
register_converter(convertors.IntConverter, 'year4')

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('cats/<int:cat_id>/', category, name='cat_id'),
    path('cats/<slug:cat_slug>/', categories_by_slug, name='cats'),
    path("stock/<year4:year>/", stock, name='stock'),
]

if settings.DEBUG:
    # errors
    urlpatterns += [
        path(r"403/", error_403),
        path(r"404/", error_404),
        path(r"500/", error_500),
    ]

handler404 = "menu_test.views.error_404"
handler500 = "menu_test.views.error_500"
