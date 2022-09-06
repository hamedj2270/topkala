# Generated by Django 4.0.3 on 2022-04-01 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('topkala_product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='نام')),
                ('slug', models.SlugField(verbose_name='نامک')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='تاربخ ثبت ')),
                ('active', models.BooleanField(default=True, verbose_name='فعال/غیرفعال')),
                ('products', models.ManyToManyField(blank=True, to='topkala_product.product', verbose_name='محصولات')),
            ],
            options={
                'verbose_name': 'برچسب/تگ',
                'verbose_name_plural': 'برچسب ها / تگ ها',
            },
        ),
    ]
