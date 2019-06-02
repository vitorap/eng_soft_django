from django.shortcuts import render, redirect, get_object_or_404
from django.http import  HttpResponse
from django.http import Http404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


from .forms import SignUpForm, ItemForm
from .models import Objeto
from .models import Usuario

'''
Objeto -> tipo, nome, descrição, usuario_dono
'''


def item_new(request):
     if request.method == "POST":
         form = ItemForm(request.POST)
         if form.is_valid():
             objeto = form.save(commit=False)
             objeto.usuario_dono = request.user
             objeto.save()
             return redirect('bemvindo')
     else:
         form = ItemForm()
     return render(request, 'item_new.html', {'form': form})

#modificar
def item_edit(request, pk):
     objeto = get_object_or_404(Objeto, pk=pk)
     if request.method == "POST":
         form = ItemForm(request.POST, instance=objeto)
         if form.is_valid():
             objeto = form.save(commit=False)
             objeto.usuario_dono = request.user
             objeto.save()
             return redirect('bemvindo')
     else:
         form = ItemForm(instance=objeto)
     return render(request, 'item_edit.html',{'form': form})

'''
def item_edit(request, pk):
     objeto = get_object_or_404(Objeto, pk=pk)
     if request.user == objeto.usuario_dono:
        if request.method == "POST":
             form = ItemForm(request.POST)
             if form.is_valid():
                 objeto = form.save(commit=False)
                 objeto.usuario_dono = request.user
                 objeto.save()
                 return redirect('bemvindo')
             else:
                 form = ItemForm(instance=objeto)
        return render(request, 'item_new.html',{'form': form})
     else:
        redirect(objeto_detail, {'pk': pk})

'''


def meusitens(request):
    itens = Objeto.objects.filter(usuario_dono = request.user)
    return render(request, 'home.html', {'objetos': itens})


def pagelogout(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')

def bemvindo(request):
    if request.user.is_authenticated:
        objetos = Objeto.objects.all()
        return render(request, 'home.html', {'objetos': objetos})
    else:
        return render(request,"bemvindo.html")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'SignUp.html', {'form': form})


def home(request):
    objetos = Objeto.objects.all()
    return render(request, 'home.html', {'objetos': objetos})

def objeto_detail(request, pk):
    try:
        objeto = Objeto.objects.get(pk=pk)
    except Objeto.DoesNotExist:
        raise Http404('Item nao encontrado')
    return render(request, 'objeto_detail.html',{'objeto': objeto})


def pedido_detail(request, id):
    return HttpResponse('<p>visao do pedido com detalhe mais o id {}</p>'.format(id))

def usuario_detail(request, id):
    try:
        usuario = Usuario.objects.get(id=id)
    except Usuario.DoesNotExist:
        raise Http404('Usuario nao encontrado')
    return render(request, 'usuario_detail.html',{'usuario': usuario})
