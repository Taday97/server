from django.http import JsonResponse
from server.models import SubProduct   
from server.models import SelectData   
from server.serializers.selectdataSerializer import SelectDataSerializer, SelectDataCreateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class Create(APIView):
    def post(self, request):
       serializeobj = SelectDataCreateSerializer(data=request.data)
       if serializeobj.is_valid():
            created_obj = serializeobj.save()
            return Response(serializeobj.data, status=201)  # Devuelve los datos del objeto creado y el estado 201
       return Response(serializeobj.errors, status=400)  # Devuelve los error
    
class GetAll(APIView):
    def get(self, request):
        detailsObj = SelectData.objects.order_by('-selectDataId').all()
        dlSerializeObj = SelectDataSerializer(detailsObj, many=True)
        return Response(dlSerializeObj.data)
    
