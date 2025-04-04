from django.urls import path, include
from .views import *

urlpatterns = [
    path('mainproduct', MainProductView.as_view(), name='mainproductView'),
    path('products/<slug:mainproduct>/', ProductsView.as_view(), name='products_view'),
    path('single-product/<slug:slug>/', SingleProductView.as_view(), name='product_view'),
]
