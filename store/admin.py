from django.contrib import admin
from django.db import models
from . import models

# Register your models here.


admin.site.register(models.Collection)


@admin.register(models.Product)
class ProdutAdmin(admin.ModelAdmin):
    list_display = ["title", "unit_price", "inventory", "inventory_status"]
    list_editable = ["unit_price"]
    list_per_page = 10

    @admin.display(ordering="inventory")
    def inventory_status(self, product):
        if product.inventory < 10:
            return "Low"
        return "OK"


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "membership"]
    list_editable = ["membership"]
    list_per_page = 10
    ordering = ["first_name", "last_name"]


# admin.site.register(models.Product, ProdutAdmin)
