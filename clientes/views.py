from django.shortcuts import render, redirect
from.models import Clientes
from.forms import ClientesForm
from django.contrib import messages


def index(request):
    clientes = Clientes.objects.all()
    context= {
        'clientes':clientes
    }
    return render(request,'clientes/index.html',context)

def ver(request, id):
    clientes = Clientes.objects.get(id=id)
    context= {
        'clientes':clientes
    }
    return render(request, 'clientes/ver.html', context)

def editar(request,id):
    clientes = Clientes.objects.get(id=id)
    if request.method == 'GET':
        form = ClientesForm(instance=clientes)
        context= {
            'form':form,
            'id':id
        }
        return render (request, 'clientes/editar.html', context)
    
    if request.method == 'POST':
        form = ClientesForm(request.POST, instance=clientes)
        if form.is_valid():
            form.save()
        context= {
            'form':form,
            'id':id
        }
        messages.success(request, 'Cliente actualizado')
        return render (request, 'clientes/editar.html', context)
    
def crear(request):
    if request.method == 'GET':
        form = ClientesForm()
        context={
            'form': form
        } 
        return render(request, 'clientes/crear.html', context)
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('clientes')
    
def borrar(request,id):
    producto=Clientes.objects.get(id=id)
    producto.delete()
    return redirect('clientes')