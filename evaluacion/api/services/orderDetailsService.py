from ..models import *
from rest_framework.response import Response
from rest_framework import status

class OrderDetailsService():
    def getAll(self):
        return Orderdetails.objects.all()
    def getByID(self, pk1, pk2):
        return Orderdetails.objects.get(orderid__orderid = pk1, productid__productid = pk2)