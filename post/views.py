from django.shortcuts import render
from post.models import Product, Review

# Create your views here.

def main(requests):
    if requests.method == 'GET':
        return render(requests, 'layosts/index.html')


def products_view(requests):
    if requests.method == 'GET':
        products = Product.objects.all()

        context = {
            'post': products
        }
        return render(requests, 'posts/post.html', context=context)


def inproducts_view(requests):
    if requests.method == 'GET':
        return render(requests, 'posts/post.html')


def product_detail_view(requests, id):
    if requests.method == 'GET':
        product = Product.objects.get(id=id)
        review = Review.objects.filter(product=product)

        context = {
            'product': product,
            'reviews': review
        }

        return render(requests, 'posts/detail.html', context=context)