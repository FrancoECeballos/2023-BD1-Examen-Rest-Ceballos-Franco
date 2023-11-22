from ..models import *
from rest_framework.response import Response
from rest_framework import status

class CustomersService():
    def getAll(self):
        return Customers.objects.all()
    def getByID(self, pk):
        return Customers.objects.get(customerid = pk)