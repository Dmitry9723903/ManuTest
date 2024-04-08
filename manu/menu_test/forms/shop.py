import pprint

from django import forms
from django.urls import reverse
from django.utils.html import format_html

from menu_test.models import Shop


class ShopForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        label="Название",
        help_text="Название магазина",
        error_messages={"required": "Укажите название"},
    )

    class Meta:
        model = Shop
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super(ShopForm, self).__init__(*args, **kwargs)

        if instance := kwargs.get("instance"):
            if instance.options:
                # распаковываем настройки магазина
                for k, v in instance.options.items():
                    if k in self.fields:
                        self.fields[k].initial = v

    def clean(self):
        """
        Проверка на доступное количество магазинов

        :return:
        """
        cleaned_data = super().clean()

        return cleaned_data

    def save(self, commit=True, *args, **kwargs):
        # сохраняем настройки магазина
        self.instance.settings = {
            k: v for k, v in self.cleaned_data.items() if k.startswith("option")
        }

        return super(ShopForm, self).save(commit=commit)
