from ..models import *
from rest_framework.response import Response
from rest_framework import status

class SuppliersService():
    def getAll(self):
        return Suppliers.objects.all()
    def getByID(self, pk):
        return Suppliers.objects.get(supplierid = pk)
        