from django.db.models import fields
from rest_framework import serializers
from server.models import SubProduct    
class SubProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubProduct  
        fields='__all__'