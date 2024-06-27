from email.mime import image
from django.shortcuts import render, redirect, get_object_or_404
from core.models import Product

def admin_panel(request):
    # Отримання усіх продуктів з БД
    products = Product.objects.all()
    return render(request, 'data/admin_panel.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        # Отримання даних з POST-запиту та збереження в БД
        name = request.POST.get('productName')
        description = request.POST.get('productDescription')
        price = request.POST.get('productPrice')
        quantity = request.POST.get('productQuantity')
        image = request.FILES.get('productImage')
        Product.objects.create(name=name, description=description, price=price, quantity=quantity, image=image)
        return redirect('admin_panel')
    return render(request, 'data/add_product.html')

def edit_product(request, product_id):
    # Отримання продукту за його ID
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.name = request.POST.get('productName')
        product.description = request.POST.get('productDescription')
        product.price = request.POST.get('productPrice')
        product.quantity = request.POST.get('productQuantity')
        if 'productImage' in request.FILES:
            product.image = request.FILES['productImage']
        # Перенаправлення на сторінку адмін панелі
        product.save()
        return redirect('admin_panel')
    return render(request, 'data/edit_product.html', {'product': product})

def delete_product(request, product_id):
    # Отримання продукту за його ID та його видалення з БД
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    # Перенаправлення на сторінку адмін панелі
    return redirect('admin_panel')


# from django.shortcuts import render, redirect, get_object_or_404
# from core.models import Product

# def admin_panel(request):
#     # Отримання усіх продуктів з БД
#     products = Product.objects.all()
#     return render(request, 'data/admin_panel.html', {'products': products})

# def add_product(request):
#     if request.method == 'POST':
#         # Отримання даних з POST-запиту та збереження в БД
#         name = request.POST.get('productName')
#         description = request.POST.get('productDescription')
#         Product.objects.create(name=name, description=description)
#         # Перенаправлення на сторінку адмін панелі
#         return redirect('/admin_panel')
#     else:
#         return render(request, 'data/admin_panel.html')

# def edit_product(request, product_id):
#     # Отримання продукту за його ID
#     product = get_object_or_404(Product, pk=product_id)
#     if request.method == 'POST':
#         # Отримання даних з POST-запиту та оновлення продукту в БД
#         product.name = request.POST.get('productName')
#         product.description = request.POST.get('productDescription')
#         product.save()
#         # Перенаправлення на сторінку адмін панелі
#         return redirect('/admin_panel')
#     else:
#         return render(request, 'data/edit_product.html', {'product': product})

# def delete_product(request, product_id):
#     # Отримання продукту за його ID та його видалення з БД
#     product = get_object_or_404(Product, pk=product_id)
#     product.delete()
#     # Перенаправлення на сторінку адмін панелі
#     return redirect('/admin_panel')
