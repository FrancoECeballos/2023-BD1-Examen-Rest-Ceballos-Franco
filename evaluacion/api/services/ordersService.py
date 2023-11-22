from ..models import *
from rest_framework.response import Response
from rest_framework import status

class OrdersService():
    def getAll(self):
        return Orders.objects.all()
    def getByID(self, pk):
        return Orders.objects.get(orderid = pk)
        