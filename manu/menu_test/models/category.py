from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)
    level = models.IntegerField(null=True)
    has_trend = models.BooleanField(default=False)

    def __str__(self):
        return self.name
