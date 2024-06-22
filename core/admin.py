from django.contrib import admin
from .models import Product, Client, Order, Payment, User

admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(User)

# Register your models here.
