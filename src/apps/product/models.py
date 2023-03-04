from django_ecommerce.common.models import BaseModel
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.urls import reverse
from apps.product import WeightUnits

# Create your models here.
class Category(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    parent = models.ForeignKey("self", null=True, blank=True, related_name="subcategory", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("category-detail", kwargs={"slug": self.slug})
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

class Product(BaseModel):
    author = models.ForeignKey(get_user_model(), related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"

class ProductMedia(BaseModel):
    product = models.ForeignKey(Product, related_name="media", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products", blank=True, null=True)
    alt = models.CharField(max_length=128, blank=True)
    
    def get_absolute_url(self):
        return reverse("product-media-detail", kwargs={"alt": self.alt})

class Collection(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True)
    products = models.ManyToManyField(Product, blank=True)
    background_image = models.ImageField(upload_to="collection-backgrounds", blank=True, null=True)
    background_image_alt = models.CharField(max_length=128, blank=True)

    description = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("product-collection-detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "product_collection"
        verbose_name_plural = "product_collections"