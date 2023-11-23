from django.shortcuts import render
from rest_framework.response import Response
from api.serializers import *
from api.models import *
from api.services.customersService import *
from api.services.categoriesService import *
from api.services.employeesService import *
from api.services.orderDetailsService import *
from api.services.ordersService import *
from api.services.productsService import *
from api.services.suppliersService import *
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

customersServ = CustomersService()
categoriesServ = CategoriesService()
employeesServ = EmployeesService()
orderDetailsServ = OrderDetailsService()
ordersServ = OrdersService()
suppliersServ = SuppliersService()
productsServ = ProductsService()

@api_view(['GET','POST'])
def customers(request):
    if request.method == 'GET':
        customers = CustomersService.getAll(customersServ)
        serializer = CustomersSerializer(customers, many=True)
        return Response(serializer.data) 
    elif request.method == 'POST':
        serializer = CustomersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def customers_id(request, pk):
    try:
        customers = CustomersService.getByID(customersServ,pk)
    except Customers.DoesNotExist:
        return Response({"message":"No existe el customer"},status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = CustomersSerializer(customers, many=False)
        return Response(serializer.data) 
    elif request.method == 'PUT':
        request.data['customerid'] = pk
        serializer = CustomersSerializer(customers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        customers.delete()
        return Response(status=status.HTTP_200_OK)
    

@api_view(['GET', 'POST'])
def suppliers(request):
    if request.method == 'GET':
        suppliers = SuppliersService.getAll(suppliersServ)
        serializer = SuppliersSerializer(suppliers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SuppliersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def suppliers_id(request, pk):
    try:
        suppliers = SuppliersService.getByID(suppliersServ,pk)
    except Suppliers.DoesNotExist:
        return Response({"message":"No existe el supplier"},status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = SuppliersSerializer(suppliers)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuppliersSerializer(suppliers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        suppliers.delete()
        return Response(status=status.HTTP_200_OK)
    

@api_view(['GET', 'POST'])
def categories(request):
    if request.method == 'GET':
        categories = CategoriesService.getAll(categoriesServ)
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def categories_id(request, pk):
    try:
        categories = CategoriesService.getByID(categoriesServ,pk)
    except Categories.DoesNotExist:
        return Response({"message":"No existe la categoría"},status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = CategoriesSerializer(categories)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CategoriesSerializer(categories, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        categories.delete()
        return Response(status=status.HTTP_200_OK)
    

@api_view(['GET', 'POST'])
def products(request):
    if request.method == 'GET':
        products = ProductsService.getAll(productsServ)
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def products_id(request, pk):
    try:
        products = ProductsService.getByID(productsServ,pk)
    except Products.DoesNotExist:
        return Response({"message":"No existe el product"},status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = ProductsSerializer(products)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductsSerializer(products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        products.delete()
        return Response(status=status.HTTP_200_OK)
    

@api_view(['GET', 'POST'])
def orders(request):
    if request.method == 'GET':
        orders = OrdersService.getAll(ordersServ)
        serializer = OrdersSerializer(orders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def orders_id(request, pk):
    try:
        orders = OrdersService.getByID(ordersServ,pk)
    except Orders.DoesNotExist:
        return Response({"message":"No existe la orden"},status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = OrdersSerializer(orders)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OrdersSerializer(orders, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        orders.delete()
        return Response(status=status.HTTP_200_OK)
    

@api_view(['GET', 'POST'])
def orderDetails(request):
    if request.method == 'GET':
        orderDetail = OrderDetailsService.getAll(orderDetailsServ)
        serializer = OrderDetailsSerializer(orderDetail, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OrderDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def orderDetails_id(request, pk1, pk2):
    try:
        orderDetail = OrderDetailsService.getByID(orderDetailsServ, pk1, pk2)
    except Orderdetails.DoesNotExist:
        return Response({"message":"No existe el detalle de orden"},status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = OrderDetailsSerializer(orderDetail)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = OrderDetailsSerializer(orderDetail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        orderDetail.delete()
        return Response(status=status.HTTP_200_OK)
    

@api_view(['GET', 'POST'])
def employees(request):
    if request.method == 'GET':
        employees = EmployeesService.getAll(employeesServ)
        serializer = EmployeesSerializer(employees, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def employees_id(request, pk):
    try:
        employees = EmployeesService.getByID(employeesServ,pk)
    except Employees.DoesNotExist:
        return Response({"message":"No existe el employee"},status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = EmployeesSerializer(employees)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EmployeesSerializer(employees, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    elif request.method == 'DELETE':
        employees.delete()
        return Response(status=status.HTTP_200_OK)



@api_view(['GET'])
def fechaMayor(request):
    orders = Orders.objects.filter(orderdate__gt="1996-12-24")
    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def fechaMenor(request):
    orders = Orders.objects.filter(orderdate__lt="1996-12-24")
    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def fechaRango(request):
    orders = Orders.objects.filter(orderdate__range=("1996-12-24","1997-1-1"))
    serializer = OrdersSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def empiezaCon(request):
    if request.method == 'GET':    
        customers = Customers.objects.filter(contactname__startswith="A")
        serializer = CustomersSerializer(customers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        letra = request.query_params.get('letra')
        customers = Customers.objects.filter(contactname__startswith=letra)
        serializer = CustomersSerializer(customers, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def terminaCon(request):
    customers = Customers.objects.filter(contactname__endswith="a")
    serializer = CustomersSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ordenado(request):
    customers = Customers.objects.all().order_by('contactname')
    serializer = CustomersSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ordenadoAlReves(request):
    customers = Customers.objects.all().order_by('-contactname')
    serializer = CustomersSerializer(customers, many=True)
    return Response(serializer.data)