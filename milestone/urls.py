from django.urls import path, include
from . import views
urlpatterns = [
    path('milestone', views.MilestoneView.as_view(), name='MilestoneView'),
]
