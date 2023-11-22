from ..models import *
from rest_framework.response import Response
from rest_framework import status

class EmployeesService():
    def getAll(self):
        return Employees.objects.all()
    def getByID(self, pk):
        return Employees.objects.get(employeeid = pk)
        