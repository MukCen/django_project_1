from django.contrib import admin
from .models import Product, Client, Order, Payment, User

admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(User)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'amount', 'method', 'status', 'payment_date']
    search_fields = ['order__id', 'method', 'status']


# Register your models here.
