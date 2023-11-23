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
    reportsto = ReportsToEmployeesSerializer(many = True)
    class Meta:
        model = Employees
        fields = '__all__'

    def create(self, validated_data):
        reportsto_data = validated_data.pop('reportsto', None)

        employee = Employees.objects.create(**validated_data)

        if reportsto_data:
            reportsto = Employees.objects.get_or_create(**reportsto_data)
            employee.reportsto = reportsto[0]

        employee.save()
        return employee

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    categoryid = CategoriesSerializer(many = False)
    supplierid = SuppliersSerializer(many = False)
    class Meta:
        model = Products
        fields = '__all__'

    def create(self, validated_data):
        supplier_data = validated_data.pop('supplierid', None)
        category_data = validated_data.pop('categoryid', None)

        product = Products.objects.create(**validated_data)

        if supplier_data:
            supplier = Suppliers.objects.get_or_create(**supplier_data)
            product.supplierid = supplier[0]

        if category_data:
            category = Categories.objects.get_or_create(**category_data)
            product.categoryid = category[0]

        product.save()
        return product

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

    def create(self, validated_data):
        customer_data = validated_data.pop('customerid', None)
        employee_data = validated_data.pop('employeeid', None)
        shipper_data = validated_data.pop('shipvia', None)

        order = Orders.objects.create(**validated_data)

        if customer_data:
            customer = Customers.objects.get_or_create(**customer_data)
            order.customerid = customer[0]

        if employee_data:
            employee = Employees.objects.get_or_create(**employee_data)
            order.employeeid = employee[0]

        if shipper_data:
            shipper = Shippers.objects.get_or_create(**shipper_data)
            order.shipvia = shipper[0]

        order.save()
        return order

class OrderDetailsSerializer(serializers.ModelSerializer):
    orderid = OrdersSerializer(many = False)
    productid = ProductsSerializer(many = False)
    class Meta:
        model = Orderdetails
        fields = '__all__'

class CustomerdemographicsSerializer(serializers.Serializer):
    customertypeid = serializers.CharField()
    customerdesc = serializers.CharField()

#Evaluación

class Punto2Serializer(serializers.Serializer):
    customertypeid = serializers.CharField()
    customerdesc = serializers.CharField()

class Punto2Serializer(serializers.ModelSerializer):
    productid = ProductsSerializer(many = False)
    class Meta:
        model = Orderdetails
        fields = '__all__'