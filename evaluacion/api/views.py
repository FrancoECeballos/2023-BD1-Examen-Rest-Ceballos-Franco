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
    elif request.method == 'POST':
        serializer = CustomersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)