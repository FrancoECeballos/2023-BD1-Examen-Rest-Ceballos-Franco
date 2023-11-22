from ..models import *
from rest_framework.response import Response
from rest_framework import status

class CategoriesService():
    def getAll(self):
        return Categories.objects.all()
    def getByID(self, pk):
        return Categories.objects.get(categoryid = pk)
        