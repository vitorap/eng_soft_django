from django.shortcuts import render, redirect, get_object_or_404
from django.http import  HttpResponse
from django.http import Http404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

from .forms import SignUpForm, ItemForm, ProfileForm
from .models import Objeto
from .models import Pedido

def dic_categorias():
    # ^^Esse dicionário serve para traduzir o display name de TIPO_CHOICES para o valor do banco de dados. 
    # Deve sempre ficar atualizado com models.py para refletir as categorias existentes.
    categorias_dict = {
    'Brinquedos' : 'B',
    'Livros' : 'L',
    'Roupas' : 'R',
    'Outros' : 'O',
    }
    return categorias_dict


def fazer_pedido(request, pk):
    objeto = get_object_or_404(Objeto, pk=pk)
    pedido = Pedido(
    usuario_interessado = request.user,
    usuario_dono = objeto.usuario_dono,
    status = Pedido.STATUS_CHOICES[0],
    data_requisito = timezone.now(),
    objeto_solicitado = objeto

        )
    pedido.save()
    return render(request,'fazer_pedido.html', {'pedido': pedido})

def aceitar_pedidos(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    pedido.status = Pedido.STATUS_CHOICES[2]
    pedido.save()
    return redirect('ver_pedido')

def recusar_pedidos(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    pedido.status = Pedido.STATUS_CHOICES[1]
    pedido.save()
    return redirect('ver_pedido')


def ver_pedido(request):
    pedidos = Pedido.objects.filter(usuario_dono = request.user)
    return render(request, 'ver_pedidos.html', {'pedidos': pedidos})

def ver_seus_pedido(request):
    pedidos = Pedido.objects.filter(usuario_interessado = request.user)
    return render(request, 'ver_seus_pedidos.html', {'pedidos': pedidos})


def item_new(request):
     if request.method == "POST":
         form = ItemForm(request.POST, request.FILES or None)
         if form.is_valid():
             objeto = form.save(commit=False)
             objeto.usuario_dono = request.user
             objeto.save()
             return render(request, 'doado_sucesso.html', {'objeto': objeto})
     else:
         form = ItemForm()
     return render(request, 'doar.html', {'form': form})


def item_doado(request):
     return render(request, 'doado_sucesso.html')

def meu_profile(request):
    return None

def ver_perdido(request):
    return None

#modifica o item somente caso o usuario seja o criador do item
def item_edit(request, pk):
     objeto = get_object_or_404(Objeto, pk=pk)
     if request.user == objeto.usuario_dono:
         if request.method == "POST":
             form = ItemForm(request.POST, instance=objeto)
             if form.is_valid():
                 objeto = form.save(commit=False)
                 objeto.usuario_dono = request.user
                 objeto.save()
                 response = HttpResponse()
                 response.write("<center><div class='alert alert-success' role='alert'>")
                 response.write(" <div class='alert alert-success' role='alert'>")
                 response.write(" <h3 class='alert-heading'> Sucesso! </h3><p> Informações Gravadas </p></div></center>")
                 return response
         else:
             form = ItemForm(instance=objeto)
         return render(request, 'item_edit.html',{'form': form})

def item_delete(request, pk):
    item = get_object_or_404(Objeto, pk=pk)
    if request.user == item.usuario_dono:
        item.delete()
    return redirect('meus_itens')

def meus_itens(request):

    objetos = Objeto.objects.filter(usuario_dono = request.user)
    categorias = []
    for objeto in objetos:
        categorias.append(objeto.get_tipo_display()) #populando categorias dos objetos existentes na database
    categorias = list(dict.fromkeys(categorias)) #remove duplicados
    filtro_categoria = False; #pro template saber se está filtrando as categorais, tb remove o carroussel
    return render(request, 'pagina_meus_itens.html', {'objetos': objetos, 'categorias': categorias, 'filtro': filtro_categoria})

def meus_itens_categoria(request, cat):
    c = dic_categorias()
    objetos = Objeto.objects.filter(usuario_dono = request.user).filter(tipo = c[cat])
    categorias = []
    for objeto in objetos:
        categorias.append(objeto.get_tipo_display()) #populando categorias dos objetos existentes na database
    categorias = list(dict.fromkeys(categorias)) #remove duplicados
    filtro_categoria = True; #pro template saber se está filtrando as categorais, tb remove o carroussel    
    return render(request, 'pagina_meus_itens.html', {'objetos': objetos, 'categorias': categorias, 'filtro': filtro_categoria})


def home(request):
    objetos = Objeto.objects.filter().exclude(usuario_dono = request.user)
    categorias = []
    for objeto in objetos:
        categorias.append(objeto.get_tipo_display()) #populando categorias dos objetos existentes na database
    categorias = list(dict.fromkeys(categorias)) #remove duplicados
    filtro_categoria = False; #pro template saber se está filtrando as categorais, tb remove o carroussel
    return render(request, 'pagina_itens.html', {'objetos': objetos, 'categorias': categorias, 'filtro': filtro_categoria})

def home_categoria(request, cat):
    c = dic_categorias()
    objetos = Objeto.objects.filter().exclude(usuario_dono = request.user).filter(tipo = c[cat])
    categorias = []
    for objeto in objetos:
        categorias.append(objeto.get_tipo_display()) #populando categorias dos objetos existentes na database
    categorias = list(dict.fromkeys(categorias)) #remove duplicados

    filtro_categoria = True; #pro template saber se está filtrando as categorais, tb remove o carroussel    
    return render(request, 'pagina_itens.html', {'objetos': objetos, 'categorias': categorias, 'filtro': filtro_categoria})


def pagelogout(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')

def bemvindo(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request,"tindoar_front_page.html")

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


def objeto_detail(request, pk):
    try:
        objeto = Objeto.objects.get(pk=pk)
    except Objeto.DoesNotExist:
        raise Http404('Item nao encontrado')
    return render(request, 'ver_item.html',{'objeto': objeto})



def usuario_detail(request, id):
    try:
        usuario = Usuario.objects.get(id=id)
    except Usuario.DoesNotExist:
        raise Http404('Usuario nao encontrado')
    return render(request, 'usuario_detail.html',{'usuario': usuario})

def edit_user(request, pk):
    user = User.objects.get(pk=pk)
    profile = user
    form = ProfileForm(instance=profile)
    if request.user.is_authenticated and request.user.id == user.id:
        if request.method == "POST":
            form = ProfileForm(request.POST, instance=profile)
            if form.is_valid():
                    update = form.save(commit=False)               
                    update.user = user
                    update.save()
                    return HttpResponse('Confirm')                
    else:
        form = UserProfileForm(instance=user)

    return render(request, 'user_edit.html', {'form': form})

def ver_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    profile = user
    return render(request, 'ver_user.html', {'user': profile})

def sobre_nos(request):
     return render(request, 'sobre.html')

def sobre_nos_noLogin(request):
     return render(request, 'sobre_NL.html')
