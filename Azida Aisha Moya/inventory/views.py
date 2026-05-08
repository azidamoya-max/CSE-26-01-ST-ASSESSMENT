from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProductForm
from .models import Product


def landing(request):
    return render(request, 'inventory/landing.html')


def product_list(request):
    form     = ProductForm()
    products = Product.objects.all().order_by('-created_at')

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product has been added successfully!')
            return redirect('product_list')
        else:
            messages.error(request, 'Please fix the errors below.')

    return render(request, 'inventory/product_list.html', {
        'form':         form,
        'products':     products,
        'total_value':  50000000,
        'total_orders': 15000000,
        'in_stock':     42000000,
        'out_of_stock': 5,
    })