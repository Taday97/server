from django.http import JsonResponse
from server.models import SubCategory   
from server.models import SubProduct   
from server.serializers.subproductsSerializer import SubProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class Create(APIView):
    def post(self,request):
       serializeobj=SubProductSerializer(data=request.data)
       if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
       return Response(serializeobj.errors) 
    
class GetAll(APIView):
    def get(self,request):
        detailsObj=SubProduct.objects.all()
        dlSerializeObj=SubProductSerializer(detailsObj, many=True)
        return Response(dlSerializeObj.data)
    def post(self,request):
        serializeobj=SubProductSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)

class GetBySubCategorieId(APIView):
    def get(self,request,subcategorieId):
       try:
           # Retrieve the product by its ID
           product = SubCategory.objects.get(pk=subcategorieId)
           # Get all associated subcategories
           detailsObj = product.subproducts.all()
       except:
           return Response("Not Found in Database")  
       
       serializeobj=SubProductSerializer(detailsObj,many=True)
       return Response(serializeobj.data)
    


class FilterByName(APIView):
    def get(self, request):
        # Get the value of the 'name' parameter from query params
        name =request.GET.get('name','')
        # Remove single or double quotes at the beginning and end, if present
        name = name.strip("'\"")
        
        # Filter products by productName containing the provide
        subProduct = SubProduct.objects.filter(subProductName__icontains=name)
        dlSerializeObj=SubProductSerializer(subProduct, many=True)
        return Response(dlSerializeObj.data)
    
