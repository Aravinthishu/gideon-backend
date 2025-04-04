from django.urls import path, include
from .views import *

urlpatterns = [
    path('category', CategoryView.as_view(), name='CategoryView'),
    path('client-logo', ClientLogoView.as_view(), name='ClientLogoView'),
]
