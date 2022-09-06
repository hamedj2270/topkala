from django.urls import path
from .views import ProductList, product_detail, SearchProductView, ProductListCategory, product_category

urlpatterns = [
    path('product', ProductList.as_view()),
    path('product/<productId>/<name>', product_detail),
    path('product/search', SearchProductView.as_view()),
    path('product/<category_name>', ProductListCategory.as_view()),
    path('product_category', product_category, name='product_category'),
]
