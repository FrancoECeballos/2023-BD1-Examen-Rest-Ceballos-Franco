from ..models import *
from rest_framework.response import Response
from rest_framework import status

class SuppliersService():
    def getAll(self):
        return Suppliers.objects.all()
    def getByID(self, pk):
        try: 
            suppliers = Suppliers.objects.get(supplierid = pk)
            return suppliers
        except Suppliers.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)