from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(
        max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed')]
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Дата створення


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(
        max_length=50,
        choices=[
            ('credit_card', 'Credit Card'),
            ('paypal', 'PayPal'),
            ('cash', 'Cash'),
        ],
    )
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    payment_date = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('completed', 'Completed'),
            ('failed', 'Failed'),
        ],
        default='pending',
    )

    def __str__(self):
        return f"Payment #{self.id} - {self.method} ({self.status})"  # type: ignore


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.CharField(
        max_length=50, choices=[('ADMIN', 'Admin'), ('MANAGER', 'Manager')]
    )


# class Payment(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     method = models.CharField(
#         max_length=50, choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal')]
#     )
