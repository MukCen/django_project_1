from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# Define BASE_DIR if it's not already defined (for example, in settings.py)
BASE_DIR = getattr(settings, 'BASE_DIR', None)

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('export/', views.export_to_excel, name='export_to_excel'),
    path('import/', views.import_from_excel, name='import_from_excel'),
    path('clients/', views.client_list, name='client_list'),
    path('orders/', views.order_list, name='order_list'),
    path('payments/', views.payment_list, name='payment_list'),
]

# # Додайте статичні та медіа маршрути, якщо MEDIA_ROOT визначено
# if BASE_DIR and settings.MEDIA_URL and settings.MEDIA_ROOT:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
