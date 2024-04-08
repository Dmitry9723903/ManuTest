from django.db import models
from django.utils import timezone

from menu_test.models.shop import Shop
from menu_test.models.category import Category


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=512)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    annotation = models.TextField(null=True)
    attributes = models.TextField(null=True)
    price = models.DecimalField(max_digits=20, decimal_places=4, null=True)
    commissions = models.TextField(null=True)
    volume_weight = models.DecimalField(max_digits=20, decimal_places=4, null=True)

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.category} / {self.name}"
