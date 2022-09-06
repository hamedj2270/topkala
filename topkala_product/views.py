import itertools
from django.shortcuts import render
from topkala_category.models import ProductCategory
# from order_module.forms import UserNewOrderForm
from topkala_order.forms import UserNewOrderForm
from . import models
from .models import Product, ProductGallery
from django.views.generic import ListView
from django.http import Http404
# from tag_module.models import Tag
# Create your views here.


# def product_page(request):
#     products:Product = models.Product.objects.all()
#     context={
#         'object_list': products
#     }
#     return render(request,'product.html',context)

class ProductList(ListView):
    paginate_by = 6
    template_name = 'product.html'
    def get_queryset(self):
        return Product.objects.get_active_products()

class ProductListCategory(ListView):
    paginate_by = 6
    template_name = 'product.html'
    def get_queryset(self):
        category_name = self.kwargs['category_name']
        category= ProductCategory.objects.filter(name__iexact=category_name).first()
        if category is None:
            raise Http404('صفحه مورد نظر یافت نشد')
        return Product.objects.get_product_by_category(category_name)
def my_grouper(n, iterable):
    args= [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def product_detail(request,*args,**kwargs):
    selected_product_id = kwargs['productId']
    user_form = UserNewOrderForm(request.POST or None , initial={'product_id':selected_product_id})
    #product_name = kwargs['name']
    product = Product.objects.get_by_id(selected_product_id)
    if product is None or not product.active:
        raise Http404('محصول مورد نظر یافت نشد')
    galleries = ProductGallery.objects.filter(product_id=selected_product_id)
    goruped_galleries = list(my_grouper(3,galleries))
    context = {
        'product': product ,
        'galleries' : goruped_galleries,
        'new_order_form' : user_form
        }
    return render(request, 'product_detail.html', context)


class SearchProductView(ListView):
    template_name = 'product.html'
    paginate_by = 6
    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.get_active_products()


def product_category(request):
    category = ProductCategory.objects.all()
    context= {
        'categories':category
    }
    return render(request,'product_categorys_partial.html',context)

