from django.urls import path
from .views import get_cities

urlpatterns = [path('cities/', get_cities)]
