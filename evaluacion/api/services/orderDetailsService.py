from ..models import *
from rest_framework.response import Response
from rest_framework import status

class OrderDetailsService():
    def getAll(self):
        return Orderdetails.objects.all()
    def getByID(self, pk1, pk2):
        return Orderdetails.objects.get(orderid__orderid = pk1, productid__productid = pk2)
    
#Evaluacion

    def punto2(self,stock, id):
        details = []
        for i in Products.objects.all():
            if i.suma() < int(stock):
                cantidad = int(stock) - i.suma()
                unitprice = i.unitprice
                if cantidad < 100:
                    orderDetail = {
                        "orderid": id,
                        "productid": i.productid,
                        "unitprice": unitprice,
                        "quantity": cantidad,
                        "discount": 0,
                    }
                else:
                    orderDetail = {
                        "orderid": id,
                        "productid": i.productid,
                        "unitprice": unitprice,
                        "quantity": cantidad,
                        "discount": 0.10,
                    }
                details.append(orderDetail)
        return details
                
        