from django.shortcuts import render
from core.models import Payment, Products, Order, Client


def dashboard(request):
    products_count = Products.objects.count()
    orders_count = Order.objects.count()
    clients_count = Client.objects.count()
    payment_count = Payment.amount

    return render(
        request,
        'web/home.html',
        {
            'products_count': products_count,
            'orders_count': orders_count,
            'clients_count': clients_count,
            'payment_count': payment_count,
        },
    )
