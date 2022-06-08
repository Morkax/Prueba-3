from django.urls import path
from .views import  Mascotas,bandanas,correas,formulario,identificaciones,home, form_Producto, form_mod_Producto, form_del_Producto

urlpatterns = [
    path('bandanas', bandanas,name= "bandanas"),
    path('correas', correas,name= "correas"),
    path('formulario', formulario,name= "formulario"),
    path('', Mascotas,name= "Mascotas"),
    path('identificaciones', identificaciones,name="identificaciones"),
    path('Mascotas', Mascotas,name= "Mascotas"),
    path('registro', home, name="home"),
    path('form-Producto', form_Producto, name="form_Producto"),
    path('form-mod-Producto/<id>', form_mod_Producto, name="form_mod_Producto"),
    path('form-del-Producto/<id>', form_del_Producto, name="form_del_Producto"),
]