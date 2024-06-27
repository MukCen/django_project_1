from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_panel, name='admin_panel'),
    path('admin/add-product/', views.add_product, name='add_product'),
    path('admin/edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('admin/delete-product/<int:product_id>/', views.delete_product, name='delete_product'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# # data/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('admin/', views.admin_panel, name='admin_panel'),
#     path('admin/add-product/', views.add_product, name='add_product'),
#     path('admin/edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
#     path('admin/delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
# ]


# from django.urls import path
# from . import views
# from django.conf import settings
# from django.conf.urls.static import static

# # Define BASE_DIR if it's not already defined (for example, in settings.py)
# BASE_DIR = getattr(settings, 'BASE_DIR', None)

# urlpatterns = [
#     path('admin/', views.admin_panel, name='admin_panel'),
#     path('edit/', views.edit_product, name='edit'),
    
# ]

# # # Додайте статичні та медіа маршрути, якщо MEDIA_ROOT визначено
# # if BASE_DIR and settings.MEDIA_URL and settings.MEDIA_ROOT:
# #     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
