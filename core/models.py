from django.db import models
from django.urls import reverse

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Назва")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "category"
        verbose_name = "Категорію"
        verbose_name_plural = "Категорії"
        ordering = ("id",)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Назва")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Опис")
    image = models.ImageField(
        upload_to="products/", blank=True, null=True, verbose_name="Відображення"
    )
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Ціна"  # type: ignore
    )
    discount = models.DecimalField(
        default=0.00, max_digits=4, decimal_places=2, verbose_name="Знижка в %"  # type: ignore
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Кількість")
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, verbose_name="Категорія"  # type: ignore
    )

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "продукти"
        ordering = ("id",)

    def __str__(self):
        return f"{self.name} Кількість - {self.quantity}"

    # def get_absolute_url(self):
    #     return reverse("catalog:product", kwargs={"product_slug": self.slug})

    def display_id(self):
        return f"{self.id:05}"  # type: ignore

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)

        return self.price


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
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
