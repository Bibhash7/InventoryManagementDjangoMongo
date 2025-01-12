from django.db import models
from inventoryManagementApp.constants import OrderStatus, StockMovementStatus
from utils.validators import custom_email_validator, phone_number_validator

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Supplier(BaseModel):
    """
    Stores supplier details

    FK (None)
    """
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True, validators=[custom_email_validator])
    phone = models.CharField(max_length=10, validators=[phone_number_validator])
    address = models.TextField(null=False,blank=False)

    def __str__(self):
        return f"{self.name} : {self.email}"

class Product(BaseModel):
    """
    Stores product details

    FK (Supplier)
    """
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=200, null=False)
    price = models.DecimalField(max_digits=12, decimal_places= 3, default=0)
    stock_quantity = models.IntegerField(default=0)
    supplier_key = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplier_product')

    def __str__(self):
        return f"{self.name} : {self.supplier_key.name} : {self.category}"

class SaleOrder(BaseModel):
    """
    Stores sales order details

    FK (None)
    """
    product_key = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_saleorder')
    quantity = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=12, decimal_places= 3, default=0)
    sale_date = models.DateField(null=False)
    status = models.CharField(
        max_length=10,
        choices=OrderStatus.choices,
        default=OrderStatus.PENDING,
    )

    def __str__(self):
        return f"{self.product_key.name} : {self.sale_date} : {self.status}"

class StockMovement(BaseModel):
    """
    Stores stock movement details

    FK (Product)
    """
    product_key = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_stock')
    quantity = models.IntegerField(default=0)
    movement_type = models.CharField(
        max_length=3,
        choices=StockMovementStatus.choices,
        default=StockMovementStatus.IN,
    )
    movement_date = models.DateField()
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.product_key.name} : {self.movement_date} : {self.movement_type}"



