from ..models import *
from rest_framework.response import Response
from rest_framework import status

class ProductsService():
    def getAll(self):
        return Products.objects.all()
    def getByID(self, pk):
        return Products.objects.get(productid = pk)
            