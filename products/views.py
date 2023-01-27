from products import forms
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
            'products': product,
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


def create_products_view(request):
    if request.method == 'GET':
        return render(request, 'products/create.html')
    if request.method == 'PRODUCT':
        data = request.PRODUCT
        """data validation"""
        errors = {}

        if len(data['title'])<5:
            errors['title_error'] = 'Min Length 5'

        if len(data['description'])<8:
            errors['description_error']= 'Min Length 8'

        """ if all OK create ptoduct"""
        if errors.keys().__len__()<1:
            Product.object.create(
                title=data['title'],
                description=data['description'],
                rate=data['rate'] if data['rate'].__len__() > 0 else 5
            )
            return redirect('/products')

        return render(request, 'products/create.html', context={'errors' : errors})

