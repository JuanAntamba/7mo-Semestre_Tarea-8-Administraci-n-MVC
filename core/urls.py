# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('admin-promos/', views.crear_promocion, name='crear_promo'),
    path('ajax/cargar-productos/', views.cargar_productos, name='ajax_cargar_productos'),
]