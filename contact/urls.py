from django.urls import path, include
from . import views

urlpatterns = [
    path('career', views.CareerView.as_view(), name='CareerView'),
    path('contact', views.ContactView.as_view(), name='ContactView'),
    path('job-position', views.JobPositionView.as_view(), name='JobPositionView'),
]
