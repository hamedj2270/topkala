# Generated by Django 4.0.3 on 2022-04-01 15:42

from django.db import migrations, models
import django.db.models.deletion
import topkala_product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='نام محصول')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='قیمت محصول')),
                ('short_description', models.CharField(max_length=200, verbose_name='توضیحات کوتاه')),
                ('description', models.TextField(verbose_name='توضیحات بیشتر')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='عکس محصول')),
                ('active', models.BooleanField(default=False, verbose_name='فعال/ غیرفعال')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('image', models.ImageField(upload_to=topkala_product.models.upload_gallery_image_path, verbose_name='عکس محصول')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topkala_product.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'تصویر',
                'verbose_name_plural': 'تصاویر',
            },
        ),
    ]
