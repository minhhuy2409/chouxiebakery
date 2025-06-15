"""
URL configuration for chouxie_project project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Không cần import views từ shop ở đây nữa, chúng ta sẽ dùng include
# from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Tất cả các URL bắt đầu bằng '' sẽ được chuyển đến file urls.py của app 'shop'
    path('', include('shop.urls')),
]

# This is important for serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)