from django.urls import path, include
from .views import *

urlpatterns = [
    path('brand', BrandView.as_view(), name='BrandView'),
    path('social-links', SocialView.as_view(), name='SocialView'),
    path('privacy-policy', PrivacyView.as_view(), name='SocialView'),
]
