from django.db import models
from django.urls import reverse # Thêm import này

class Cake(models.Model):
    CAKE_TYPE_CHOICES = [
        ('WHIPPING', 'Whipping'),
        ('SPONGE', 'Sponge'),
        ('GENOISE', 'Genoise'),
        ('CHIFFON', 'Chiffon'),
        ('TIRAMISU', 'Tiramisu'),
    ]

    name = models.CharField(max_length=200, verbose_name="Tên bánh")
    description = models.TextField(verbose_name="Mô tả")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Giá")
    image = models.ImageField(upload_to='cakes/', verbose_name="Hình ảnh")
    cake_type = models.CharField(max_length=50, choices=CAKE_TYPE_CHOICES, verbose_name="Loại bánh")
    color = models.CharField(max_length=50, blank=True, verbose_name="Màu sắc")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
       
        return reverse('cake_detail', kwargs={'pk': self.pk})