from django.shortcuts import render
from rest_framework.response import Response
from api.serializers import *
from api.models import *
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET','POST'])
def customers(request):
    if request.method == 'GET':
        customers = Customers.objects.all()
        serializer = CustomersSerializer(customers, many=True)
        return Response(serializer.data)