from django.urls import path, include
from . import views

urlpatterns = [
    path('Who-we-are-section', views.WhoWeAreSectionView.as_view(), name='WhoWeAreSectionView'),
    path('our-mission-vision', views.OurMissionVisionView.as_view(), name='OurMissionVisionView'),
    path('our-values', views.OurValuesView.as_view(), name='OurValuesView'),
]
