from django.db.models.query import QuerySet
from shop.models import Shop, Warehouse, Stock

def shop_list() -> QuerySet[Shop]:
    qs = Shop.objects.select_related("user").all()
    return qs

def warehouse_list() -> QuerySet[Warehouse]:
    qs = Warehouse.objects.select_related("shop").all()
    return qs

def stock_list() -> QuerySet[Stock]:
    qs = Stock.objects.select_related("warehouse","product").all()
    return qs