from django.contrib import admin
from inventoryManagementApp.models import Supplier, Product, SaleOrder, StockMovement
# Register your models here.

class SaleOrderInterface(admin.ModelAdmin):
    list_filter = ('status',)
    list_per_page = 10

class ProductInterface(admin.ModelAdmin):
    list_filter = ('category',)
    list_per_page = 10

class SupplierInterface(admin.ModelAdmin):
    list_per_page = 10

class StockMovementInterface(admin.ModelAdmin):
    list_filter = ('movement_type',)
    list_per_page = 10

admin.site.register(Supplier, SupplierInterface)
admin.site.register(Product, ProductInterface)
admin.site.register(SaleOrder, SaleOrderInterface)
admin.site.register(StockMovement, StockMovementInterface)