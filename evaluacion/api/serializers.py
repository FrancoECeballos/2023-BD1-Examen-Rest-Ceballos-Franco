from api.models import *
from rest_framework import serializers

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'

class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = '__all__'

class ReportsToEmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'

class EmployeesSerializer(serializers.ModelSerializer):
    reportsto = ReportsToEmployeesSerializer(many = False)
    class Meta:
        model = Employees
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class ShippersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shippers
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
    customerid = CustomersSerializer(many = False)
    employeeid = EmployeesSerializer(many = False)
    shipvia = ShippersSerializer(many = False)
    class Meta:
        model = Orders
        fields = '__all__'

class OrderDetailsSerializer(serializers.ModelSerializer):
    orderid = OrdersSerializer(many = False)
    productid = ProductsSerializer(many = False)
    class Meta:
        model = Orderdetails
        fields = '__all__'