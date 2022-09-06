from django.db.models import Q
import os.path
import random
from django.db import models
import os
# Create your models here.
# from category_module.models import ProductCategory


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"


def upload_gallery_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/galleries{final_name}"


class ProductManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def get_product_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name, active=True).distinct()

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tag__title__icontains=query)

        )
        return self.get_queryset().filter(lookup, active=True).distinct()


class Product(models.Model):
    # slug  = models.SlugField(blank=True)
    title = models.CharField(max_length=200, verbose_name='نام محصول')
    price = models.DecimalField(verbose_name='قیمت محصول', max_digits=10, decimal_places=2)
    short_description = models.CharField(max_length=200, verbose_name='توضیحات کوتاه')

    description = models.TextField(verbose_name='توضیحات بیشتر')

    image = models.ImageField(verbose_name='عکس محصول', upload_to='images/', null=True, blank=True, )
    active = models.BooleanField(default=False, verbose_name='فعال/ غیرفعال')
    # categories = models.ManyToManyField(ProductCategory, blank=True, verbose_name='دسته بندی ها')

    objects = ProductManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return f'{self.title}({self.price}(تومان'

    def get_absolute_url(self):
        return f"/product/{self.id}/{self.title.replace(' ', '-')}"

    def get_product_image(self):
        if self.image is not None:
            return self.image.url
        return ''


class ProductGallery(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    image = models.ImageField(verbose_name='عکس محصول', upload_to=upload_gallery_image_path)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'

    def __str__(self):
        return self.title
