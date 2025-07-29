from django.urls import path
from .views import *




urlpatterns = [
    path('order', create_order_view, name='order'),
    # path('seats', seats, name='seats'),
]