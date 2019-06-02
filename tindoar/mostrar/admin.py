from django.contrib import admin

from .models import Usuario
from .models import Objeto
from .models import Pedido

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['login','nome','telefone','sex']

@admin.register(Objeto)
class ObjetoAdmin(admin.ModelAdmin):
    list_display = ['nome','tipo','usuario_dono']

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['usuario_interessado','usuario_dono','status','data_requisito']
