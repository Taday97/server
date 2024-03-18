from django.db.models import fields
from rest_framework import serializers
from server.models import SelectData, Product,SubCategory,SubProduct  
class SelectDataCreateSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), many=True)
    subCategory = serializers.PrimaryKeyRelatedField(queryset=SubCategory.objects.all(), many=True)
    subProducts = serializers.PrimaryKeyRelatedField(queryset=SubProduct.objects.all(), many=True)

    class Meta:
        model = SelectData
        fields = ['selectDataId', 'product', 'subCategory', 'subProducts']

    def create(self, validated_data):
        products = validated_data.pop('product')
        subCategories = validated_data.pop('subCategory')
        subProducts = validated_data.pop('subProducts')
        selectData = SelectData.objects.create(**validated_data)
        selectData.product.set(products)
        selectData.subCategory.set(subCategories)
        selectData.subProducts.set(subProducts)
        return selectData

    def update(self, instance, validated_data):
        instance.product.set(validated_data.get('product', instance.product.all()))
        instance.subCategory.set(validated_data.get('subCategory', instance.subCategory.all()))
        instance.subProducts.set(validated_data.get('subProducts', instance.subProducts.all()))
        instance.save()
        return instance
      
class SelectDataSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    subCategory = serializers.SerializerMethodField()
    subProducts = serializers.SerializerMethodField()

    class Meta:
        model = SelectData
        fields = ['selectDataId','product', 'subCategory', 'subProducts']

    def get_product(self, obj):
        return [product.productName for product in obj.product.all()]

    def get_subCategory(self, obj):
        return [subCategory.subCategoryName for subCategory in obj.subCategory.all()]

    def get_subProducts(self, obj):
        return [subProduct.subProductName for subProduct in obj.subProducts.all()]