# shop/apps.py

from django.apps import AppConfig

class ShopConfig(AppConfig):  # Tên class phải là ShopConfig
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'  