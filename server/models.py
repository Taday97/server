from django.db import models
  
class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=255)

    def __str__(self):
        return self.productName
    
class SubCategory(models.Model):
    subCategoryId = models.AutoField(primary_key=True)
    subCategoryName = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.subCategoryName

class SubProduct(models.Model):
    subProductId = models.AutoField(primary_key=True)
    subProductName = models.CharField(max_length=255)
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='subproducts')
    def __str__(self):
        return self.subProductName
    
class SelectData(models.Model):
    selectDataId = models.AutoField(primary_key=True)
    product = models.ManyToManyField(Product, related_name='selectdata')
    subCategory = models.ManyToManyField(SubCategory, related_name='selectdata')
    subProducts = models.ManyToManyField(SubProduct, related_name='selectdata')
    def __str__(self):
     product_names = ', '.join([product.productName for product in self.product.all()])
     sub_category_names = ', '.join([subCategory.subCategoryName for subCategory in self.subCategory.all()])
     sub_product_names = ', '.join([subProduct.subProductName for subProduct in self.subProducts.all()])
     return f"{product_names} / {sub_category_names} / {sub_product_names}"