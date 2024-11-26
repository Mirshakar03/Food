from pyexpat.errors import messages

from django.shortcuts import render
from apps.product.models import Product


def product_list_view(request):
    products = Product.objects.all().count()
    return render(request, 'menu.html', {'products': products})
