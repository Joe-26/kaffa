from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_view, name='menu'),
    path('product/<int:item_id>', views.product_view, name='product'),
    path('add-to-cart', views.addToCart, name='addToCart'),
    path('delete-cart-item/<int:cartItem_id>', views.deleteCartItem, name='deleteCartItem'),
    path('cart', views.cart_view, name='cart'),
    path('order',views.confirmOrder, name='order'),
]