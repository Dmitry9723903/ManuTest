from django.shortcuts import render, reverse, HttpResponseRedirect, get_object_or_404
from django.views import View
from django.contrib import messages
from menu_test.handler import ShopHandler
from menu_test.models import Shop
from menu_test.forms import ShopForm

TITLES = {
    Shop: {
        "list": "Магазины",
        "update": "Изменение магазина",
        "update_success": "Магазин успешно сохранен",
        "not_found": "Магазин не найден",
        "delete_success": "Магазин удален",
        "delete_error": "Ошибка удаления магазина",
    },
}


class ShopListView(View):
    model = Shop
    url_list = "shops"
    template_name = "shops/list.html"

    def get(self, request, *args, **kwargs):
        # shop = get_object_or_404(Shop, pk=kwargs["pk"])
        # shop = Shop.objects.all()
        # data = {
        #     "shop": shop.name,
        #
        # }
        items = Shop.objects.all()
        return render(
            request,
            self.template_name,
            {"title": TITLES[self.model]["list"], "list": items},
        )

    def post(self, request, *args, **kwargs):
        shop_id = request.POST.get("shop_id", 0)

        return HttpResponseRedirect(reverse(self.url_list))


class ShopFormView(View):
    model = Shop
    model_form = ShopForm
    url_list = "shops"
    template_name = "shops/form.html"

    def get(self, request, *args, **kwargs):
        entry_id = kwargs.get("entry_id", 0)
        request.session[f"{self.url_list}_previous_url"] = request.META.get(
            "HTTP_REFERER"
        )

        try:
            obj = self.model.objects.get(id=entry_id)
        except self.model.DoesNotExist:
            obj = None

        form = self.model_form(instance=obj)
        return render(
            request,
            self.template_name,
            {"title": TITLES[self.model]["update"], "obj": obj, "form": form},
        )

    def post(self, request, *args, **kwargs):
        entry_id = kwargs.get("entry_id", 0)
        shop_handler = ShopHandler()
        new_shop = shop_handler.create_shop()

        try:
            obj = self.model.objects.get(id=entry_id)
        except self.model.DoesNotExist:
            obj = None

        form = ShopForm(request.POST or None, instance=obj)

        if form.is_valid():
            messages.add_message(
                request,
                messages.INFO,
                TITLES[self.model]["update_success"],
                extra_tags="success",
            )
            obj = form.save()
            return HttpResponseRedirect(
                request.session.get(
                    f"{self.url_list}_previous_url", reverse(self.url_list)
                )
            )
        else:
            messages.error(
                request,
                f"Форма содержит ошибки: {form.errors}",
                extra_tags="danger",
            )
            return render(
                request,
                self.template_name,
                {"title": TITLES[self.model]["update"], "obj": obj, "form": form},
            )

    def delete(self, request, *args, **kwargs):
        entry_id = kwargs.get("entry_id", 0)
        try:
            obj = self.model.objects.get(id=entry_id)
            obj.delete()
            messages.add_message(
                request,
                messages.INFO,
                TITLES[self.model]["delete_success"],
                extra_tags="info",
            )
        except self.model.DoesNotExist:
            messages.add_message(
                request,
                messages.ERROR,
                TITLES[self.model]["not_found"],
                extra_tags="danger",
            )

        return HttpResponseRedirect(reverse(self.url_list))

