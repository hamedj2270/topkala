from django.db import models


# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان ')
    link = models.URLField(max_length=400, verbose_name='لینک', null=True, blank=True)
    image = models.ImageField(verbose_name='بارگذاری تصویر بنر', upload_to='images/banner', null=True, blank=True)
    active = models.BooleanField(verbose_name='فعال/ غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تنظیمات بنر'
        verbose_name_plural = 'مدیریت بنر'


class AsideBanner(models.Model):
    class SiteBannerPositions(models.TextChoices):
        product_list ='home', 'صفحه اصلی'

    title = models.CharField(max_length=150, verbose_name='عنوان')
    link = models.URLField(max_length=400, verbose_name='لینک بنر', null=True, blank=True)
    image = models.ImageField(verbose_name='بارگذاری تصویر بنر 272px*406px', upload_to='images/banner/aside-banner',
                              null=True, blank=True)
    active = models.BooleanField(verbose_name='فعال/ غیرفعال')
    position=models.CharField(max_length=200,choices=SiteBannerPositions.choices , verbose_name='جایگاه نمایش')
    def __str__(self):
        return self.title



    class Meta:
        verbose_name = "بنر حاشیه "
        verbose_name_plural = 'بنر حاشیه سایت'

    # def get_product_image(self):
    #     if self.image is not None:
    #         return self.image.url
    #     return ''
