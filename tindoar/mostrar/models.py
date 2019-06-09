from django.db import models
from django.contrib.auth.models import User
#chave primaria é criada por padrao no django, entao nao precisa especificar aqui

class Usuario(models.Model):
    SEX_CHOICES = [('M','Masculino'),('F','Feminino')]
    login = models.EmailField(max_length=254)
    nome = models.CharField(max_length=100)
    telefone = models.IntegerField(null=False)
    sex = models.CharField(choices=SEX_CHOICES,max_length=1)
    def __str__(self):
        return self.nome

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Objeto(models.Model):
    TIPO_CHOICES = [('L','Livros'),('B','Brinquedos'),('R','Roupas'),('O','Outros')]
    tipo = models.CharField(choices=TIPO_CHOICES,max_length=2, default='O')
    nome = models.CharField(max_length=100)
    descrição = models.TextField(max_length=500)
    usuario_dono = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to= upload_location, null=True, blank=True, width_field="largura_img", height_field="altura_img")
    altura_img = models.IntegerField(default=0)
    largura_img = models.IntegerField(default=0)
    def __str__(self):
        return self.nome

class Pedido(models.Model):
    STATUS_CHOICES = [('E','Espera'),('R','Recusado'),('A','Aprovado')]
    usuario_interessado = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='interessado')
    usuario_dono = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='dono')
    data_requisito = models.DateTimeField()
    status = models.CharField(choices=STATUS_CHOICES,max_length=1)
    objeto_solicitado = models.ForeignKey(Objeto, on_delete=models.CASCADE)