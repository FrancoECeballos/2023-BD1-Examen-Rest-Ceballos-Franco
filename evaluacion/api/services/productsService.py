from ..models import *
from rest_framework.response import Response
from rest_framework import status

class ProductsService():
    def getAll(self):
        return Products.objects.all()
    def getByID(self, pk):
        try: 
            products = Products.objects.get(productid = pk)
            return products
        except Products.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)