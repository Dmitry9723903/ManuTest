import pprint

from django.db import models
from django.contrib import admin


class Shop(models.Model):
    name = models.CharField(max_length=256)

    options = models.JSONField(null=True, blank=True)

    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    @admin.display(description="Name", ordering="name")
    def shop_name(self):
        return str(self)
