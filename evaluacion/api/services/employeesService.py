from ..models import *
from rest_framework.response import Response
from rest_framework import status

class EmployeesService():
    def getAll(self):
        return Employees.objects.all()
    def getByID(self, pk):
        try: 
            employees = Employees.objects.get(employeeid = pk)
            return employees
        except Employees.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)