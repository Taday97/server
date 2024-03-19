"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from server.views import productsView
from server.views import subcategoriesView
from server.views import subproductsView
from server.views import selectdataView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', selectdataView.GetAll.as_view()),

    # Routes for'Products'
    path('products', productsView.GetAll.as_view()),
    path('products/filter/', productsView.FilterByName.as_view()),#subproducts/filter/?name=
    
    # Routes for'Subcategories'
    path('subcategories', subcategoriesView.GetAll.as_view()),
    path('productId/<int:productId>/subcategories', subcategoriesView.GetByProductId.as_view()),
    path('subcategories/filter/', subcategoriesView.FilterByName.as_view()),#subproducts/filter/?name=

    # Routes for'SubProducts'
    path('subproducts', subproductsView.GetAll.as_view()),
    path('subcategorieId/<int:subcategorieId>/subproducts', subproductsView.GetBySubCategorieId.as_view()),
    path('subproducts/filter/',subproductsView.FilterByName.as_view()),#subproducts/filter/?name=
    path('subproducts/create/',subproductsView.Create.as_view()),#Create Subproduct By Body {"subCategory": 1,"subProductName": "Age11","subProductId":0}

    # Routes for'SelectData'
    path('selectdata', selectdataView.GetAll.as_view()),
    path('selectdata/create/',selectdataView.Create.as_view()),#Create Select Data By Body {"product": [1],"subCategory": [3],"subProducts": [1, 4]}
]
