import os
from django.db import models
from topkala_category.models import ProductCategory
# Create your models here.
from topkala_tag.models import Tag


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"


class Slider(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    link = models.URLField(max_length=100, verbose_name='لینک')
    description = models.TextField(verbose_name='توضیحات')
    categories = models.ManyToManyField(ProductCategory, blank=True, verbose_name='دسته بندی')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='برچسب')
    image = models.ImageField(verbose_name='بارگذاری تصویر اسلایدر', upload_to='images/slider', null=True, blank=True)
    active = models.BooleanField(default=False, verbose_name='فعال/ غیرفعال')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'

    def __str__(self):
        return self.title
