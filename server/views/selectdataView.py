from server.models import SelectData   
from server.serializers.selectdataSerializer import SelectDataSerializer, SelectDataCreateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# POST method for creating a new Data Select
class Create(APIView):
    def post(self, request):
       serializeobj = SelectDataCreateSerializer(data=request.data)
       if serializeobj.is_valid():
            serializeobj.save()
            return Response(serializeobj.data, status=201) 
       return Response(serializeobj.errors, status=400)

# GET method to retrieve all Data Select    
class GetAll(APIView):
    def get(self, request):
        detailsObj = SelectData.objects.order_by('-selectDataId').all()
        dlSerializeObj = SelectDataSerializer(detailsObj, many=True)
        return Response(dlSerializeObj.data)
    
