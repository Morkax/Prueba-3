from django.urls import path
from .views import home, form_Producto, form_mod_Producto, form_del_Producto

urlpatterns = [
    path('', home, name="home"),
    path('form-Producto', form_Producto, name="form_Producto"),
    path('form-mod-Producto/<id>', form_mod_Producto, name="form_mod_Producto"),
    path('form-del-Producto/<id>', form_del_Producto, name="form_del_Producto"),
]