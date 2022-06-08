from django.urls import path
from rest_producto.views import lista_productos

urlpatterns =[
    path('lista_productos', lista_productos, name="lista_productos"),
]