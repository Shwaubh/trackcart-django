from django.urls import path
from .views import price

urlpatterns = [
    path('price', price, name='get-price')
]