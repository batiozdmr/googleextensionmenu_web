from django.contrib import admin

from apps.product.models import *

admin.site.register(ProductCategory)
admin.site.register(Products)
