from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
#chave primaria é criada por padrao no django, entao nao precisa especificar aqui

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Objeto(models.Model):
    TIPO_CHOICES = [('AN','Animais De Estimação'),('BQ','Brinquedos'),('ED','Eletrodomésticos'),('EL','Eletrônicos'),('FR','Ferramentas'),('IC','Itens Para Casa'),('IM','Instrumentos Musicais'),('JT','Jogos de Tabuleiro'),('LI','Livros'),('ME','Material de Estudo'),('MB','Mobília'),('PC','Perfumes e Cosméticos'),('RV','Roupas e Vestuário'),('SD','Saúde e Medicina'),('JV','Videogame'),('OT','Outros')]
    tipo = models.CharField(choices=TIPO_CHOICES,max_length=2, default='OT')
    nome = models.CharField(max_length=100)
    descrição = models.TextField(max_length=500)
    usuario_dono = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to= upload_location, null=True, blank=True, width_field="largura_img", height_field="altura_img")
    altura_img = models.IntegerField(default=0)
    largura_img = models.IntegerField(default=0)
    def __str__(self):
        return self.nome

# deleta a imagem quando o objeto é apagado\/
@receiver(post_delete, sender=Objeto) 
def submission_delete(sender, instance, **kwargs):
    instance.imagem.delete(False) 

class Pedido(models.Model):
    STATUS_CHOICES = [('E','Espera'),('R','Recusado'),('A','Aprovado')]
    usuario_interessado = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='interessado')
    usuario_dono = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='dono')
    data_requisito = models.DateTimeField()
    status = models.CharField(choices=STATUS_CHOICES,max_length=1)
    objeto_solicitado = models.ForeignKey(Objeto, on_delete=models.CASCADE)