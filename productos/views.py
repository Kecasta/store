from django.shortcuts import render, redirect
from.models import Productos
from.forms import ProductosForm
from django.contrib import messages

def index(request):
    productos = Productos.objects.all()
    context= {
        'productos':productos
    }
    return render(request,'productos/index.html',context)

def ver(request, id):
    productos = Productos.objects.get(id=id)
    context= {
        'productos':productos
    }
    return render(request, 'productos/ver.html', context)

def editar(request,id):
    productos = Productos.objects.get(id=id)
    if request.method == 'GET':
        form = ProductosForm(instance=productos)
        context= {
            'form':form,
            'id':id
        }
        return render (request, 'productos/editar.html', context)
    
    if request.method == 'POST':
        form = ProductosForm(request.POST, instance=productos)
        if form.is_valid():
            form.save()
        context= {
            'form':form,
            'id':id
        }
        messages.success(request, 'Producto actualizado')
        return render (request, 'productos/editar.html', context)
   
def crear(request):
    if request.method == 'GET':
        form = ProductosForm()
        context={
            'form': form
        } 
        return render(request, 'productos/crear.html', context)
    if request.method == 'POST':
        form = ProductosForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('productos')

def borrar(request,id):
    producto=Productos.objects.get(id=id)
    producto.delete()
    return redirect('productos')
