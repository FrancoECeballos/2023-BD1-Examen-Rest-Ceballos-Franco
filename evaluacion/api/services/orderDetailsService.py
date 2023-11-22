from ..models import *
from rest_framework.response import Response
from rest_framework import status

class OrderDetailsService():
    def getAll(self):
        return Orderdetails.objects.all()
    def getByID(self, pk1, pk2):
        try: 
            orderDetails = Orderdetails.objects.get(orderid__orderid = pk1, productid__productid = pk2)
            return orderDetails
        except Orderdetails.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)