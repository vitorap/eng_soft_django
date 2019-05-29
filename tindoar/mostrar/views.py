from django.shortcuts import render
from django.http import  HttpResponse
from django.http import Http404

from .models import Objeto
from .models import Usuario


def home(request):
    objetos = Objeto.objects.all()
    return render(request, 'home.html', {'objetos': objetos})

def objeto_detail(request, id):
    try:
        objeto = Objeto.objects.get(id=id)
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
