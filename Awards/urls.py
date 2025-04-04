from django.urls import path, include
from . import views

urlpatterns = [
    path('awards', views.AwardsView.as_view(), name='AwardsView'),
    path('testimonial', views.TestimonialView.as_view(), name='TestimonialView'),
]
