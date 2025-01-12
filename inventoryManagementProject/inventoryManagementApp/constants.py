from django.db import models


class OrderStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    COMPLETED = 'COMPLETED', 'Completed'
    CANCELLED = 'CANCELLED', 'Cancelled'


class StockMovementStatus(models.TextChoices):
    IN = 'IN', 'In'
    OUT = 'OUT', 'Out'

class SuccessMessage:
    SUCCESS = "Success"
    DATA_CREATED_SUCCESSFULLY = "Data {}: Created."

class ErrorMessage:
    ERROR = "Error"
    MANDATORY_FIELD_MISSING = "Please provide all fields."
    INTERNAL_SERVER_ERROR = "Internal Server Error."
    DATA_ALREADY_EXIST = "This data already exists."
    NOT_ENOUGH_PRODUCTS_OR_PRICE_MISMATCH = "Not enough products or price mismatch."


class SupplierAttributes:
    NAME = "name"
    EMAIL = "email"
    PHONE = "phone"
    ADDRESS = "address"
    EMPTY_STRING = ""

class ProductAttributes:
    NAME = "name"
    DESCRIPTION = "description"
    CATEGORY = "category"
    PRICE = "price"
    STOCK_QUANTITY = "stock_quantity"
    SUPPLIER_KEY = "supplier_key"
    EMPTY_STRING = ""

class StockMovementAttributes:
    PRODUCT_KEY = "product_key"
    QUANTITY = "quantity"
    MOVEMENT_TYPE = "movement_type"
    MOVEMENT_DATE = "movement_date"
    NOTES = "notes"
    EMPTY_STRING = ""

class SaleOrderAttributes:
    PRODUCT_KEY = "product_key"
    QUANTITY = "quantity"
    TOTAL_PRICE = "total_price"
    SALE_DATE = "sale_date"
    STATUS = "status"
    EMPTY_STRING = ""
