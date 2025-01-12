from inventoryManagementApp.models import Supplier, Product, SaleOrder
from rest_framework.serializers import ModelSerializer


class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SaleOrderSerializer(ModelSerializer):
    class Meta:
        model = SaleOrder
        fields = '__all__'
