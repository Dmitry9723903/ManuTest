import random
import string
from django.utils import timezone
from .models import Shop


class ShopHandler:
    @staticmethod
    def generate_random_string(length=10):
        """Генерирует случайную строку заданной длины."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    @staticmethod
    def create_shop():
        """Создает экземпляр модели Shop с случайными данными и сохраняет его в базе данных."""
        name = ShopHandler.generate_random_string()
        options = {'key1': 'value1', 'key2': 'value2'}
        is_active = random.choice([True, False])
        created_at = timezone.now()
        updated_at = timezone.now()

        shop = Shop.objects.create(name=name, options=options, is_active=is_active, created_at=created_at,
                                   updated_at=updated_at)
        return shop
