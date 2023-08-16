from django.shortcuts import render, redirect
from .models import Cart
from administrator.models import post
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='accounts:login')
def cart_view(request):
    card = Cart.objects.filter(user_id=request.user.user_id)
    user = request.user
    total = 0
    for cards in card:
        total += cards.quantity * cards.product.price

    context ={
        'card': card,
        'total': total,
        'user': user
    }
    return render(request, 'cart/shopping-cart.html', context)


@login_required(login_url='accounts:login')
def add_to_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    quantity =1

    if Cart.objects.filter(user_id=request.user.user_id, product_id=id).exists():
        card=Cart.objects.get(user_id=request.user.id, product_id=id)
        card.quantity += 1
        card.save()
        return redirect(url)
    else:
        card = Cart.objects.create(quantity=quantity, product_id=id, user_id=request.user.user_id)

        card.save()
        return redirect(url)


@login_required(login_url='accounts:login')
def remove_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    card = Cart.objects.get(id=id)
    card.delete()
    return redirect(url)

@login_required(login_url='accounts:login')
def add_single(request, id):
    url = request.META.get('HTTP_REFERER')
    cart = Cart.objects.get(id=id)
    prudoct = post.objects.get(id=cart.product.id)
    if prudoct.count > cart.quantity:
        cart.quantity += 1
        cart.save()
        return redirect(url)
    else:
        return redirect(url)


@login_required(login_url='accounts:login')
def remove_single(request, id):
    url = request.META.get('HTTP_REFERER')
    cart = Cart.objects.get(id=id)
    if cart.quantity < 2:
        cart.delete()
        return redirect(url)
    else:
        cart.quantity-=1
        cart.save()
        return redirect(url)