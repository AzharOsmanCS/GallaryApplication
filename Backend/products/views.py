from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product, Seller, Category
from .serializer import ProductSerializer, ProductsAllInfoSerializer, CategorySerializer, SellerSerializer

class ProductList(APIView):
    """""
    List all products or create new one

    """
    def get(self, request):
        products = Product.objects.all()
        #Serializer
# Create your views here.
#API In Django
#1. model
#2. view
#3. URl
#4. Seralizer (Through JSON) object data