from ..models import *
from rest_framework.response import Response
from rest_framework import status

class OrderDetailsService():
    def getAll(self):
        return Orderdetails.objects.all()
    def getByID(self, pk):
        try: 
            orderDetails = Orderdetails.objects.get(orderid__orderid = pk)
            return orderDetails
        except Orderdetails.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)