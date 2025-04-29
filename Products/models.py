from django.db import models
# Create your models here.
from base.models import BaseModel


class Category( BaseModel ):

    category_name = models.CharField( max_length= 100)
    slug = models.SlugField( unique= True , null=True , blank=True)
    category_image = models.ImageField( upload_to= "Categories")


class Products( BaseModel):

    product_name = models.CharField( max_length= 100)
    slug = models.SlugField( unique= True , null=True , blank=True)

    category = models.ForeignKey( Category , on_delete=models.CASCADE , related_name="products")
    price = models.IntegerField()
    product_description = models.TextField()
    


class ProductImage(BaseModel):

    product = models.ForeignKey(Products , on_delete=models.CASCADE , related_name="productimage")
    image = models.ImageField( upload_to= "product")