from django.contrib import admin
from .models import Category, Item, CartItem, Order, OrderItem

# Register your models here.
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)