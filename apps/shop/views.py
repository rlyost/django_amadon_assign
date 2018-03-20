from django.shortcuts import render, redirect
from time import gmtime, strftime

def index(request):
    if 'shop' not in request.session:
        item1 = { 'item': 'Dojo Tshirt', 'price': 19.99, 'product_id': 1001 }
        item2 = { 'item': 'Dojo Sweater', 'price': 29.99, 'product_id': 1002 }
        item3 = { 'item': 'Dojo Cup', 'price': 4.99, 'product_id': 1003 }
        item4 = { 'item': 'Algorithm Book', 'price': 49.99, 'product_id': 1004 }
        request.session['shop'] = [item1, item2, item3, item4]
    return render(request, 'shop/index.html', all_items=request.session['shop'])

def buy(request):
    if request.method == "POST":
        product_id = request.POST['product_id']
        quantity = request.POST['quantity']
        for item in request.session['shop']:
            if item['product_id'] == product_id:
                cart = quantity * item['price']
        request.session['life_dollars'] += request.session['cart']
        request.session['life_items'] += quantity
        request.session['context'] = [cart, request.session['life_items'], request.session['life_dollars']]
    return redirect("/checkout", request.session['context'])

def checkout(request):
    return render(request, 'shop/checkout.html', request.session['context'])