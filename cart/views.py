from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

def cart_summary(request):
    return render(request, "cart/cart_summary.html", {})

def cart_add(request):
    cart = Cart(request)
    #test Post
    if request.POST == 'post':
        #get stuff
        product_id = int(request.POST.get('product_id'))
        #look product in the DB
        product = get_object_or_404(Product, id=product_id)
        #Save to session
        cart.add(product=product)
        #return response
        response = JsonResponse({'Product Name: ': product.name})
        return response

def cart_delete(request):
    pass

def cart_update(request):
    pass