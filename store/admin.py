from typing import Reversible
from django.contrib import admin
from django.contrib.admin.filters import SimpleListFilter
from django.db import models
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.urls import reverse
from django.db.models.aggregates import Count
from django.utils.html import format_html, urlencode
from . import models

# Register your models here.


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ["title", "product_count"]

    @admin.display(ordering="product_count")
    def product_count(self, collection):
        url = (
            reverse("admin:store_product_changelist")
            + "?"
            + urlencode({"collection__id": str(collection.id)})
        )
        return format_html("<a href={}>{}</>", url, collection.product_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(product_count=Count("product"))


class InventoryFilter(admin.SimpleListFilter):
    title = "inventory"
    parameter_name = "inventory"

    def lookups(self, request, model_admin):
        return [("<10", "Low")]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == "<10":
            return queryset.filter(inventory__lt=10)


@admin.register(models.Product)
class ProdutAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "unit_price",
        "inventory",
        "inventory_status",
        "collection_title",
    ]
    list_editable = ["unit_price"]
    list_filter = ["collection", "last_update", InventoryFilter]
    list_per_page = 10
    list_select_related = ["collection"]

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering="inventory")
    def inventory_status(self, product):
        if product.inventory < 10:
            return "Low"
        return "OK"


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership", "order_count"]
    list_editable = ["membership"]
    list_per_page = 10
    ordering = ["first_name", "last_name"]
    search_fields = ["first_name__istartswith", "last_name__istartswith"]

    @admin.display(ordering="order_count")
    def order_count(self, customer):
        url = (
            reverse("admin:store_order_changelist")
            + "?"
            + urlencode(
                {
                    "customer__id": str(customer.id),
                }
            )
        )
        return format_html("<a href={}>{} Orders</>", url, customer.order_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(order_count=Count("order"))


# admin.site.register(models.Product, ProdutAdmin)


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "placed_at", "customer", "payment_status"]
