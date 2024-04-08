from django.conf import settings
from django.urls import path, re_path, register_converter
from . import convertors
from . import views as mt_views
register_converter(convertors.IntConverter, 'year4')

urlpatterns = [
    path('', mt_views.home, name='home'),
    # Shops
    path('shop/', mt_views.ShopListView.as_view(), name='shop'),
    re_path(
        r"^shop/(?P<entry_id>\d+)/",
        mt_views.ShopFormView.as_view(),
        name="shop_form",
    ),
    re_path(
        r"^shop/delete/(?P<entry_id>\d+)/",
        mt_views.ShopFormView().delete,
        name="shop_delete",
    ),
    # Categories
    path('category/', mt_views.category, name='category'),
    # path('cats/<int:cat_id>/', category, name='cat_id'),
    # path('cats/<slug:cat_slug>/', categories_by_slug, name='cats'),
    # path("stock/<year4:year>/", stock, name='stock'),
    # Products
    # path('product/', mt_views.product, name='category'),
    # Stocks
]

if settings.DEBUG:
    # errors
    urlpatterns += [
        path(r"403/", mt_views.error_403),
        path(r"404/", mt_views.error_404),
        path(r"500/", mt_views.error_500),
    ]

handler404 = "menu_test.views.error_404"
handler500 = "menu_test.views.error_500"
