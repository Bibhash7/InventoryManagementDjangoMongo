import logging
from dateutil import parser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from inventoryManagementApp.constants import (
    SuccessMessage,
    ErrorMessage,
    SupplierAttributes,
    ProductAttributes,
    StockMovementAttributes,
    SaleOrderAttributes,
    OrderStatus,
    StockMovementStatus,
)
from inventoryManagementApp.models import Supplier, Product, SaleOrder, StockMovement
from inventoryManagementApp.serializer import (
    SupplierSerializer,
    ProductSerializer,
    SaleOrderSerializer,
)
from django.db import IntegrityError

# Create your views here.

logger = logging.getLogger(__name__)


@api_view(["POST"])
def add_supplier(request):
    """
    Adds a supplier in the Supplier model
    :param name (Str):
    :param email (Str):
    :param phone (Str):
    :param address (Str):
    :return Response:
    """

    try:
        name = request.data.get(
            SupplierAttributes.NAME, SupplierAttributes.EMPTY_STRING
        )
        email = request.data.get(
            SupplierAttributes.EMAIL, SupplierAttributes.EMPTY_STRING
        )
        phone = request.data.get(
            SupplierAttributes.PHONE, SupplierAttributes.EMPTY_STRING
        )
        address = request.data.get(
            SupplierAttributes.ADDRESS, SupplierAttributes.EMPTY_STRING
        )

        if name and email and phone and address:
            Supplier(name=name, email=email, phone=phone, address=address).save()
            return Response(
                {
                    SuccessMessage.SUCCESS: SuccessMessage.DATA_CREATED_SUCCESSFULLY.format(
                        name
                    )
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {ErrorMessage.ERROR: ErrorMessage.MANDATORY_FIELD_MISSING},
                status=status.HTTP_400_BAD_REQUEST,
            )
    except IntegrityError as error:
        logger.error(error)
        return Response(
            {ErrorMessage.ERROR: ErrorMessage.DATA_ALREADY_EXIST},
            status=status.HTTP_400_BAD_REQUEST,
        )
    except Exception as error:
        logger.error(error)
        return Response(
            {ErrorMessage.ERROR, ErrorMessage.INTERNAL_SERVER_ERROR},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET"])
def list_supplier(request):
    """
    Shows all suppliers
    :param request (None):
    :return Response:
    """

    try:
        suppliers = Supplier.objects.all()
        supplier_serializer = SupplierSerializer(suppliers, many=True)
        return Response(
            {SuccessMessage.SUCCESS: supplier_serializer.data},
            status=status.HTTP_200_OK,
        )
    except Exception as error:
        logger.error(error)
        return Response(
            {ErrorMessage.ERROR, ErrorMessage.INTERNAL_SERVER_ERROR},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
def add_product(request):
    """
    Adds a Product in the Product model
    :param name (Str):
    :param description (Str):
    :param category (Str):
    :param price (Float):
    :param stock_quantity (Int):
    :param supplier_key (Int):
    :return Response:
    """

    try:
        name = request.data.get(ProductAttributes.NAME, ProductAttributes.EMPTY_STRING)
        description = request.data.get(
            ProductAttributes.DESCRIPTION, ProductAttributes.EMPTY_STRING
        )
        category = request.data.get(
            ProductAttributes.CATEGORY, ProductAttributes.EMPTY_STRING
        )
        price = float(request.data.get(ProductAttributes.PRICE, 0))
        stock_quantity = int(request.data.get(ProductAttributes.STOCK_QUANTITY, 0))
        supplier_key = int(request.data.get(ProductAttributes.SUPPLIER_KEY, 0))

        if (
            name
            and description
            and category
            and price
            and stock_quantity
            and supplier_key
        ):
            Product(
                name=name,
                description=description,
                category=category,
                price=price,
                stock_quantity=stock_quantity,
                supplier_key=Supplier.objects.get(id=supplier_key),
            ).save()
            return Response(
                {
                    SuccessMessage.SUCCESS: SuccessMessage.DATA_CREATED_SUCCESSFULLY.format(
                        name
                    )
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {ErrorMessage.ERROR: ErrorMessage.MANDATORY_FIELD_MISSING},
                status=status.HTTP_400_BAD_REQUEST,
            )
    except IntegrityError as error:
        logger.error(error)
        return Response(
            {ErrorMessage.ERROR: ErrorMessage.DATA_ALREADY_EXIST},
            status=status.HTTP_400_BAD_REQUEST,
        )
    except Exception as error:
        logger.error(error)
        return Response(
            {ErrorMessage.ERROR, ErrorMessage.INTERNAL_SERVER_ERROR},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET"])
def list_product(request):
    """
    Shows all Products
    :param request (None):
    :return Response:
    """

    try:
        products = Product.objects.all()
        product_serializer = ProductSerializer(products, many=True)
        return Response(
            {SuccessMessage.SUCCESS: product_serializer.data}, status=status.HTTP_200_OK
        )
    except Exception as error:
        logger.error(error)
        return Response(
            {ErrorMessage.ERROR, ErrorMessage.INTERNAL_SERVER_ERROR},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
def add_stock_movement(request):
    """
    Adds stock movement
    :param product_key (Str):
    :param quantity (Int):
    :param movement_type (Str):
    :param movement_date (Date):
    :param product_key (Str):
    :return Response:
    """
    try:
        product_key = request.data.get(
            StockMovementAttributes.PRODUCT_KEY, StockMovementAttributes.EMPTY_STRING
        )
        quantity = int(request.data.get(StockMovementAttributes.QUANTITY, 0))
        movement_type = request.data.get(
            StockMovementAttributes.MOVEMENT_TYPE, StockMovementAttributes.EMPTY_STRING
        )
        movement_date = parser.parse(request.data.get(
            StockMovementAttributes.MOVEMENT_DATE, StockMovementAttributes.EMPTY_STRING
            )
        )
        notes = request.data.get(
            StockMovementAttributes.NOTES, StockMovementAttributes.EMPTY_STRING
        )

        if product_key and quantity and movement_type and movement_date and notes:
            StockMovement(
                product_key=Product.objects.get(id=product_key),
                quantity=quantity,
                movement_type=movement_type,
                movement_date=movement_date,
                notes=notes,
            ).save()
            return Response(
                {
                    SuccessMessage.SUCCESS: SuccessMessage.DATA_CREATED_SUCCESSFULLY.format(
                        ""
                    )
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {ErrorMessage.ERROR: ErrorMessage.MANDATORY_FIELD_MISSING},
                status=status.HTTP_400_BAD_REQUEST,
            )
    except IntegrityError as error:
        logger.error(error)
        return Response(
            {ErrorMessage.ERROR: ErrorMessage.DATA_ALREADY_EXIST},
            status=status.HTTP_400_BAD_REQUEST,
        )
    except Exception as error:
        logger.error(error)
        return Response(
            {ErrorMessage.ERROR, ErrorMessage.INTERNAL_SERVER_ERROR},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
def create_sale_order(request):
    """
    Create a Sale order by user.
    :param product_key (Int):
    :param quantity (Int):
    :param total_price (Int):
    :param sale_date (Date):
    :return Response:
    """
    try:
        product_key = int(request.data.get(
            StockMovementAttributes.PRODUCT_KEY, SaleOrderAttributes.EMPTY_STRING
            )
        )
        quantity = int(request.data.get(SaleOrderAttributes.QUANTITY, 0))
        total_price = int(request.data.get(
            SaleOrderAttributes.TOTAL_PRICE, SaleOrderAttributes.EMPTY_STRING
            )
        )
        sale_date = parser.parse(request.data.get(
            SaleOrderAttributes.SALE_DATE, SaleOrderAttributes.EMPTY_STRING
            )
        )

        if product_key and quantity and total_price and sale_date:
            products = Product.objects.get(id=product_key)
            if (
                products.stock_quantity >= quantity
                and total_price >= products.price * products.stock_quantity
            ):
                products.stock_quantity -= quantity
                products.save()
                SaleOrder(
                    product_key=Product.objects.get(id=product_key),
                    quantity=quantity,
                    total_price=total_price,
                    sale_date=sale_date,
                    status=OrderStatus.COMPLETED,
                ).save()
                return Response(
                    {
                        SuccessMessage.SUCCESS: SuccessMessage.DATA_CREATED_SUCCESSFULLY.format(
                            ""
                        )
                    },
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {
                        ErrorMessage.ERROR: ErrorMessage.NOT_ENOUGH_PRODUCTS_OR_PRICE_MISMATCH
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(
                {ErrorMessage.ERROR: ErrorMessage.MANDATORY_FIELD_MISSING},
                status=status.HTTP_400_BAD_REQUEST,
            )
    except IntegrityError as error:
        logger.error(error)
        return Response(
            {ErrorMessage.ERROR: ErrorMessage.DATA_ALREADY_EXIST},
            status=status.HTTP_400_BAD_REQUEST,
        )
    except Exception as error:
        logger.error(error)
        return Response(
            {ErrorMessage.ERROR, ErrorMessage.INTERNAL_SERVER_ERROR},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["POST"])
def cancel_sale_order(request):
    """
    Create a Sale order by user.
    :param product_key (Int):
    :param sale_order_key (Int):
    :return Response:
    """
    try:
        product_key = int(request.data.get(
            StockMovementAttributes.PRODUCT_KEY, SaleOrderAttributes.EMPTY_STRING
            )
        )
        sale_order_key = request.data.get("sale_order_key")
        if product_key and sale_order_key:
            product = Product.objects.get(id=product_key)
            sale_order = SaleOrder.objects.get(id=sale_order_key)
            product.stock_quantity += sale_order.quantity
            sale_order.status = OrderStatus.CANCELLED
            product.save()
            sale_order.save()
        else:
            return Response(
                {ErrorMessage.ERROR: ErrorMessage.MANDATORY_FIELD_MISSING},
                status=status.HTTP_400_BAD_REQUEST,
            )
    except IntegrityError as error:
        logger.error(error)
        return Response(
            {ErrorMessage.ERROR: ErrorMessage.DATA_ALREADY_EXIST},
            status=status.HTTP_400_BAD_REQUEST,
        )
    except Exception as error:
        logger.error(error)
        return Response(
            {ErrorMessage.ERROR, ErrorMessage.INTERNAL_SERVER_ERROR},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET"])
def list_orders(request):
    """
    Shows all Orders
    :param request (None):
    :return Response:
    """

    try:
        sale_order = SaleOrder.objects.all()
        sale_order_serializer = SupplierSerializer(sale_order, many=True)
        return Response(
            {SuccessMessage.SUCCESS: sale_order_serializer.data},
            status=status.HTTP_200_OK,
        )
    except Exception as error:
        logger.error(error)
        return Response(
            {ErrorMessage.ERROR, ErrorMessage.INTERNAL_SERVER_ERROR},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
