from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [

    path('', views.allProdCat, name="allProdCat"),
    path('<slug:c_slug/>', views.allProdCat(name='products_by_category')),



]
