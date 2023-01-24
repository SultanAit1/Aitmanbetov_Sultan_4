
from django.shortcuts import render
from products.models import Product, Review, Category


def main(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        category_id = request.GET.get('category')
        if category_id:
            products = Product.objects.filter(category=Category.objects.get(id=category_id))
        else:
            products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'products/products.html', context=context)

def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def inproducts_view(request):
    if request.method == 'GET':
        return render(request, 'products/products.html')


def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        review = Review.objects.filter(product=product)

        context = {
            'product': product,
            'reviews': review,
        }

        return render(request, 'products/detail.html', context=context)

def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories,
        }

        return render(request, 'categories/index.html', context=context)
