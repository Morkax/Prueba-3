from django.shortcuts import render, redirect
from django.template import loader
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def home(request):
    producto = Producto.objects.all()
    datos = {
        'producto': producto
    }
    return render(request, 'core/home.html', datos)

def form_Producto(request):
    datos = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"

    return render(request, 'core/form_Producto.html', datos)

def form_mod_Producto(request, id):
    producto = Producto.objects.get(Producto=id)
    datos = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificados correctamente"
    return render(request, 'core/form_mod_Producto.html', datos)

def form_del_Producto(request, id):
    producto = Producto.objects.get(Id=id)
    producto.delete() 
    return redirect(to="home")