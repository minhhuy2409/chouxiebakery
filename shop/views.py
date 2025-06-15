from django.shortcuts import render, get_object_or_404
from .models import Cake

def cake_list(request):
    cakes = Cake.objects.all().order_by('-created_at') # Sắp xếp bánh mới nhất lên đầu
    cake_types = Cake.CAKE_TYPE_CHOICES

    # Logic tìm kiếm
    search_query = request.GET.get('q')
    if search_query:
        cakes = cakes.filter(name__icontains=search_query)

    # Logic lọc
    filter_type = request.GET.get('type')
    if filter_type:
        cakes = cakes.filter(cake_type=filter_type)

    context = {
        'cakes': cakes,
        'cake_types': cake_types, # Gửi danh sách loại bánh ra template để tạo bộ lọc
        'current_filter': filter_type, # Để active nút filter
    }
    return render(request, 'shop/cake_list.html', context)


def cake_detail(request, pk):
    # Lấy đối tượng bánh với id=pk, nếu không có sẽ trả về lỗi 404
    cake = get_object_or_404(Cake, pk=pk)
    context = {
        'cake': cake
    }
    return render(request, 'shop/cake_detail.html', context)