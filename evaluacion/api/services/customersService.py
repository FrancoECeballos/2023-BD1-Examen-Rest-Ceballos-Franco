from ..models import *
from rest_framework.response import Response
from rest_framework import status

class CustomersService():
    def getAll(self):
        return Customers.objects.all()
    def getByID(self, pk):
        try: 
            customers = Customers.objects.get(customerid = pk)
            return customers
        except Customers.DoesNotExist():
            return Response(status=status.HTTP_404_NOT_FOUND)