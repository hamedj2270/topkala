from django.db import models


# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    name = models.CharField(max_length=150, verbose_name='نامک')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title

# class MainMenu(models.Model):
#     title = models.CharField(max_length=150,verbose_name='عنوان')
#     link = models.URLField(max_length=100, verbose_name='لینک')
