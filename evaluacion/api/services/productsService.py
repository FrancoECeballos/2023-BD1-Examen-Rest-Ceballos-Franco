from ..models import *
from rest_framework.response import Response
from rest_framework import status

class ProductsService():
    def getAll(self):
        return Products.objects.all()
    def getByID(self, pk):
        return Products.objects.get(productid = pk)
    
    #Evaluacion

    def punto1(self,supid,catid,stock):
        resultados = []
        prods = Products.objects.filter(supplierid=supid, categoryid=catid, discontinued=False)
        for i in prods:
            if i.suma() < int(stock):
                stockfinal = i.suma()
                guardar = {
                    "productid": i.productid,
                    "productname": i.productname,
                    "stockFinal": stockfinal,
                    "unitprice": i.unitprice
                }
                resultados.append(guardar)
                
        return resultados