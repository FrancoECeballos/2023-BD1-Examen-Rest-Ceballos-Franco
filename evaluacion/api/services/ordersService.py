from ..models import *
from rest_framework.response import Response
from rest_framework import status

class OrdersService():
    def getAll(self):
        return Orders.objects.all()
    def getByID(self, pk):
        try: 
            orders = Orders.objects.get(orderid = pk)
            return orders
        except Orders.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)