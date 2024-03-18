from django.http import JsonResponse
from server.models import SubCategory   
from server.models import Product   
from server.serializers.subcategoriesSerializer import SubCategoriesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class GetAll(APIView):
    def get(self,request):
        detailsObj=SubCategory.objects.all()
        dlSerializeObj=SubCategoriesSerializer(detailsObj, many=True)
        return Response(dlSerializeObj.data)

class GetByProductId(APIView):
    def get(self,request,productId):
       try:
           # Retrieve the product by its ID
           product = Product.objects.get(pk=productId)
           # Get all associated subcategories
           detailsObj = product.subcategories.all()
       except:
           return Response("Not Found in Database")  
       
       serializeobj=SubCategoriesSerializer(detailsObj,many=True)
       return Response(serializeobj.data)

class FilterByName(APIView):
    def get(self, request):
        # Get the value of the 'name' parameter from query params
        name =request.GET.get('name','')
        # Remove single or double quotes at the beginning and end, if present
        name = name.strip("'\"")
        
        # Filter products by productName containing the provide
        subCategory = SubCategory.objects.filter(subCategoryName__icontains=name)
        dlSerializeObj=SubCategoriesSerializer(subCategory, many=True)
        return Response(dlSerializeObj.data)
    
