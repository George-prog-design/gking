from django.urls import path
from . import views


urlpatterns = [
    path('',  views.store, name='store'),
    path('cart/',  views.cart, name='cart'),
    path('checkout/',  views.checkout, name='check-out'),
    path('restaurant/',  views.restaurant, name='restaurant'),
    path('restaurant/<str:slug>', views.restaurantview, name='restaurantview'),
    path('restaurant/<str:MenuItem_id>/<str:Hotel_id>', views.menuitemview, name='menuitemview'),
    path('view/',  views.View, name='view'),
    path('about/',  views.About, name='about'),
    path('help/',  views.Help, name='help'),
    path('services/',  views.Services, name='services'),
    path('maps/',  views.Maps, name='maps'),


]