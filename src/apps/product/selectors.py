from django.db.models.query import QuerySet
from product.models import Category, Product, ProductMedia, Collection

def category_list() -> QuerySet[Category]:
    qs = Category.objects.select_related("parent").all()
    return qs

def product_list() -> QuerySet[Product]:
    qs = Product.objects.select_related("author", "category").all()
    return qs

def product_media_list() -> QuerySet[ProductMedia]:
    qs = ProductMedia.objects.select_related("product").all()
    return qs

def collection_list() -> QuerySet[Collection]:
    qs = Collection.objects.prefetch_related("products").all()
    return qs