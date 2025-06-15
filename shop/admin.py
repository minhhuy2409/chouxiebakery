from django.contrib import admin
from .models import Cake
from django.utils.html import format_html # Thêm import này

# Tạo một class tùy chỉnh cho trang admin của Cake
@admin.register(Cake) # Decorator is a cleaner way to register
class CakeAdmin(admin.ModelAdmin):
    # Các cột sẽ hiển thị ở danh sách
    list_display = ('image_tag', 'name', 'cake_type', 'price', 'created_at')
    # Thêm bộ lọc ở bên phải
    list_filter = ('cake_type',)
    # Thêm thanh tìm kiếm
    search_fields = ('name', 'description')

    # Hàm để hiển thị ảnh thumbnail
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 70px; max-height: 70px; border-radius: 8px;" />', obj.image.url)
        return "No Image"
    image_tag.short_description = 'Ảnh' # Đặt tên cho cột