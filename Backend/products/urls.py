from django.urls import path
from .views import ProductList, CategoryViewSet, SellerViewSet


urlpatterns = [
    path('products', ProductList.as_view())
]