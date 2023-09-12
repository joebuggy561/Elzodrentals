from django.db import models
from django.contrib.auth.models import User



class CarCategories(models.Model):
    vehicle_type = models.CharField(max_length=50)
    car_name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    description = models.TextField(max_length=500)
    car_year = models.IntegerField()
    car_image = models.ImageField(upload_to='photo/carcategories', blank=True)

    class Meta:
        verbose_name = 'carcategory'
        verbose_name_plural = 'carcategories'


    def __str__(self):
        return self.vehicle_type 



class Products(models.Model):
    category = models.ForeignKey(CarCategories, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50, unique=False)
    slug = models.SlugField(max_length=250, unique=True)
    product_model = models.CharField(max_length=50)
    product_year = models.CharField(max_length=50)
    product_sit = models.CharField(max_length=50)
    product_transmission = models.CharField(max_length=50)
    product_doors = models.CharField(max_length=50)
    product_price_day = models.IntegerField(default=0)
    product_price_week = models.IntegerField(default=0)
    product_price_month = models.IntegerField(default=0)
    product_images = models.ImageField(upload_to='photo/products', blank=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
    

    def __str__(self):
        return self.product_name


# Create your models here.
