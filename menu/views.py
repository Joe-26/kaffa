from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Item, CartItem, Order, OrderItem
from django.utils import timezone # Import timezone
from users.models import User # Assuming User is your custom user model

# Create your views here.
def menu_view(request):
    items = Item.objects.all()
    context = {'items':items}
    return render(request, 'menu.html', context)

def product_view(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {'product': item}
    return render(request, 'product.html', context)

@login_required
def cart_view(request):
    items = Item.objects.all()
    cartItems = CartItem.objects.filter(user=request.user)

    context = {}
    cartItemsLoad = []

    subTotal = 0
    for cartItem in cartItems:
        for item in items:
            if cartItem.item.name == item.name:
                subTotal += float(item.price)*float(cartItem.quantity)
                cartItemsLoad.append({'id':cartItem.id, 'drink':item.name,'quantity': cartItem.quantity, 'perPrice':float(item.price), 'subSubTotal':float(item.price*cartItem.quantity)})
    context['cartItems'] = cartItemsLoad
    context['SubTotal'] = round(subTotal, 2)
    tax_rate = 0.06 # Example tax rate of 3%
    context['Tax'] = round(subTotal * tax_rate, 2)
    context['Total'] = round(subTotal + (subTotal * tax_rate), 2)

    '''
    {
        "cartItems": [
            {
                "drink":"Dark Roast",
                "quantity":2,
                "perPrice":2.59,
                "subSubTotal":5.18
            },
            {
                "drink":"Latte",
                "quantity":1,
                "perPrice":3.59,
                "subSubTotal":3.59
            }
        ],
        "SubTotal": 90,
        "Tax": 10,
        "Total": 100
    }
    '''
    return render(request, 'cart.html', context)

@login_required
def addToCart(request):
    if request.method == 'POST':
        logged_user = request.POST.get('user_id')
        drink = request.POST.get('product_id')
        # size = request.POST.get('size')
        quantity = request.POST.get('quantity-input')
        username = get_object_or_404(User, pk=logged_user)
        drinkName = get_object_or_404(Item, pk=drink)
        print('Received Cart Item:', username, drinkName, quantity)
        try:
            cartItem = CartItem(
                user=username,
                item=drinkName,
                quantity=quantity
            )
            cartItem.save()
            print('Saved item in Cart!')
            messages.success(request, 'Added to Cart!')
            return redirect('menu')
        except Exception as e:
            print(request, f'An error occurred: {e}')
            return render(request, 'product.html', request.POST)
    else:
        messages.warning(request, "Invalid request method for adding to cart.")
        return redirect('menu')

@login_required
def deleteCartItem(request, cartItem_id):
    print('Received Args: ', cartItem_id)
    try:
        cartItem = get_object_or_404(CartItem, pk=cartItem_id)
        print('Deleting - ',cartItem)
        cartItem.delete()
        messages.success(request, 'Item removed from cart.')
        return redirect('cart')
    except:
        messages.warning(request, "Invalid request method for deleting cart item.")

    return render(request, 'cart.html')

@login_required
def confirmOrder(request):
    context = {}
    if request.method == 'POST':
        current_user = request.user
        cart_items = CartItem.objects.filter(user=current_user)

        if not cart_items.exists():
            messages.error(request, "Your cart is empty. Please add items before placing an order.")
            return redirect('cart')

        # Recalculate total amount for security and consistency
        sub_total = 0
        for cart_item in cart_items:
            sub_total += cart_item.item.price * cart_item.quantity
        
        tax_rate = 0.06  # Example tax rate of 3% - should ideally be a setting
        tax_amount = round(float(sub_total) * tax_rate, 2)
        total_amount = round(float(sub_total) + float(tax_amount), 2)

        try:
            # Create the Order
            order = Order.objects.create(
                user=current_user,
                order_date=timezone.now(),
                total_amount=total_amount,
                status='pending'
            )

            # Create OrderItems from CartItems
            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    item=cart_item.item,
                    quantity=cart_item.quantity,
                    unit_price=cart_item.item.price
                )
            
            # Clear the cart for the user
            cart_items.delete()
            messages.success(request, "Your order has been placed successfully!")
            orders = Order.objects.filter(user=request.user)
            #orderItems = OrderItem.objects.filter()
            context = {'orders':orders}
            print('Context: ', context)
            return render(request, 'order.html', context)
        except Exception as e:
            messages.error(request, f"An error occurred while placing your order: {e}")
            return redirect('cart')
    # For GET request, just render the order confirmation page
    orders = Order.objects.filter(user=request.user)
    context['orders'] = orders
    print('Context2: ', context)
    return render(request, 'order.html', context)