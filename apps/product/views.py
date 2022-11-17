from django.shortcuts import render

from apps.product.models import *


def product_api(request):
    products = Products.objects.filter()
    product_category = ProductCategory.objects.filter()
    context = {
        'products': products,
        'product_category': product_category,
    }
    return render(request, "apps/files/get_file_api.html", context)
