from django.shortcuts import render, redirect

def index(request):
    if 'shop' not in request.session:
        item1 = { 'item': 'Dojo Tshirt', 'price': 19.99, 'product_id': 1001 }
        item2 = { 'item': 'Dojo Sweater', 'price': 29.99, 'product_id': 1002 }
        item3 = { 'item': 'Dojo Cup', 'price': 4.99, 'product_id': 1003 }
        item4 = { 'item': 'Algorithm Book', 'price': 49.99, 'product_id': 1004 }
        request.session['life_dollars'] = 0
        request.session['life_items'] = 0
        request.session['shop'] = [item1, item2, item3, item4]
    return render(request, 'shop/index.html')

def buy(request):
    if request.method == "POST":
        request.session['cart'] = 0
        product_id = int(request.POST['product_id'])
        quantity = int(request.POST['quantity'])
        for item in request.session['shop']:
            if int(item['product_id']) == product_id:
                request.session['cart'] = quantity * item['price']
        request.session['life_dollars'] += request.session['cart']
        request.session['life_items'] += quantity
    return redirect("/checkout")

def checkout(request):
    return render(request, 'shop/checkout.html')