from server.models import Product   
from server.serializers.productsSerializer import ProductsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
 
 # GET method to retrieve all Products
class GetAll(APIView):
    def get(self,request):
        detailsObj=Product.objects.all()
        dlSerializeObj=ProductsSerializer(detailsObj, many=True)
        return Response(dlSerializeObj.data)
    def post(self,request):
        serializeobj=ProductsSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)

# FilterByName method filters Products by their name based on the 'name' query parameter.
class FilterByName(APIView):
    def get(self, request):
        # Get the value of the 'name' parameter from query params
        name =request.GET.get('name','')
        # Remove single or double quotes at the beginning and end, if present
        name = name.strip("'\"")
        
        # Filter products by productName containing the provide
        products = Product.objects.filter(productName__icontains=name)
        dlSerializeObj=ProductsSerializer(products, many=True)
        return Response(dlSerializeObj.data)
   
