from django.db.models import fields
from rest_framework import serializers
from server.models import Product    
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product  
        fields='__all__'