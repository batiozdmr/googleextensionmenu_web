from django.urls import path

from .views import *

app_name = "files"

urlpatterns = [
    path('get/products/', product_api, name='product_api'),

]
