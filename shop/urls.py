from django.urls import path
from . import views

urlpatterns = [
    # URL cho trang danh sách sản phẩm (trang chủ)
    path('', views.cake_list, name='cake_list'),

    # URL cho trang chi tiết sản phẩm, ví dụ: /cake/1/
    path('cake/<int:pk>/', views.cake_detail, name='cake_detail'),
]