from django.contrib import admin
from .models import Product
from .models import SubCategory
from .models import SubProduct
from .models import SelectData

class DetailsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, DetailsAdmin)
admin.site.register(SubCategory, DetailsAdmin)
admin.site.register(SubProduct, DetailsAdmin)
admin.site.register(SelectData, DetailsAdmin)
# Register your models here.    