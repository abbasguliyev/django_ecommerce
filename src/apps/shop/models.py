from django.db import models
from django_ecommerce.common.models import BaseModel
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

# Create your models here.
class Shop(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="shop")
    slug = models.SlugField(max_length=255, unique=True)
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="logo", null=True, blank=True)

    def get_absolute_url(self):
        return reverse("shop-detail", kwargs={"slug": self.slug})
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "shop"
        verbose_name_plural = "shops"

class Warehouse(BaseModel):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=255, unique=True)
    address = models.TextField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="warehouses")

    def get_absolute_url(self):
        return reverse("warehouse-detail", kwargs={"slug": self.slug})
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "warehouse"
        verbose_name_plural = "warehouses"

class Stock(BaseModel):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name="stocks")
    product = models.ForeignKey("product.Product", on_delete=models.CASCADE, related_name="stocks")