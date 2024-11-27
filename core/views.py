from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse, HttpResponse

from core.forms import PaymentForm
from .models import Product, Client, Order, Payment
import openpyxl
from django.utils.encoding import smart_str
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os


def product_list(request):
    products = Product.objects.all()
    return render(request, 'core/product_list.html', {'products': products})


def export_to_excel(request):
    # Create a workbook and add a worksheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Products"

    # Define the titles for columns
    columns = ['Name', 'Description', 'Price', 'Quantity']
    ws.append(columns)

    # Fetch data from the database and append it to the worksheet
    products = Product.objects.all()
    for product in products:
        ws.append([product.name, product.description, product.price, product.quantity])

    # Prepare the response and save the file in memory
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=products.xlsx'
    wb.save(response)  # type: ignore

    return response


def import_from_excel(request):
    if request.method == 'POST' and request.FILES['import_file']:
        import_file = request.FILES['import_file']
        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'uploads'))
        filename = fs.save(import_file.name, import_file)
        filepath = fs.path(filename)

        wb = openpyxl.load_workbook(filepath)
        ws = wb.active

        for row in ws.iter_rows(min_row=2, values_only=True):  # Skip the header row
            name, description, price, quantity = row
            Product.objects.create(
                name=name, description=description, price=price, quantity=quantity
            )

        # Delete the file after processing
        os.remove(filepath)

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'fail', 'message': 'No file uploaded'})


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'core/client_list.html', {'clients': clients})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'core/order_list.html', {'orders': orders})


def payment_list(request):
    payments = Payment.objects.select_related('order').all()
    return render(request, 'core/payment_list.html', {'payments': payments})


def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                'payment_success'
            )  # Направляє на сторінку успішного додавання
    else:
        form = PaymentForm()
    return render(request, 'core/add_payment.html', {'form': form})


def order_details(request, order_id):
    # Отримання замовлення за його ID
    order = get_object_or_404(Order, id=order_id)

    # Отримання інформації про оплату (якщо є)
    payment = Payment.objects.filter(order=order).first()

    context = {
        'order': order,
        'payment': payment,
    }
    return render(request, 'core/order_details.html', context)


# def payment_list(request):
#     payments = Payment.objects.all()
#     return render(request, 'core/payment_list.html', {'payments': payments})
