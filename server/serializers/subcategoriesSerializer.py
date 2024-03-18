from django.db.models import fields
from rest_framework import serializers
from server.models import SubCategory  
class SubCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubCategory  
        fields='__all__'