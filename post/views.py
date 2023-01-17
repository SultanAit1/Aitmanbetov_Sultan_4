from django.shortcuts import HttpResponse, render
from datetime import datetime
from post.models import Product


# Create your views here.


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layosts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': products
        }

        return render(request, 'posts/post.html', context=context)
