from django.urls import path
from .views import *
app_name='cart'
urlpatterns=[
    path('', cart_view, name='cart_view'),
    path('add_to_cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('remove_cart/<int:id>/', remove_cart, name='remove_cart'),
    path('add_single/<int:id>/', add_single, name='add_single'),
    path('remove_single/<int:id>/', remove_single, name='remove_single'),

]