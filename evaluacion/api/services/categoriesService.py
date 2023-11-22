from ..models import *
from rest_framework.response import Response
from rest_framework import status

class CategoriesService():
    def getAll(self):
        return Categories.objects.all()
    def getByID(self, pk):
        try: 
            categories = Categories.objects.get(categoryid = pk)
            return categories
        except Categories.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)