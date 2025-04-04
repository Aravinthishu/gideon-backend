from django.urls import path, include
from . import views

urlpatterns = [
    path('expertise/', views.ExpertiseView.as_view(), name='ExpertiseView'),
    path('ceo/', views.CeosDeskView.as_view(), name='CeosDeskView'),
]
