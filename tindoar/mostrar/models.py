from django.db import models

#chave primaria é criada por padrao no django, entao nao precisa especificar aqui

class Usuario(models.Model):
    SEX_CHOICES = [('M','Masculino'),('F','Feminino')]
    login = models.EmailField(max_length=254)
    nome = models.CharField(max_length=100)
    telefone = models.IntegerField(null=False)
    sex = models.CharField(choices=SEX_CHOICES,max_length=1)
    def __str__(self):
        return self.nome

class Objeto(models.Model):
    TIPO_CHOICES = [('L','Livros'),('B','Brinquedos'),('R','Roupas'),('O','Outros')]
    tipo = models.CharField(choices=TIPO_CHOICES,max_length=1)
    nome = models.CharField(max_length=100)
    descrição = models.TextField()
    usuario_dono = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    STATUS_CHOICES = [('E','Espera'),('R','Recusado'),('A','Aprovado')]
    usuario_interessado = models.ForeignKey(Usuario, on_delete=models.CASCADE,  related_name='interessado')
    usuario_dono = models.ForeignKey(Usuario, on_delete=models.CASCADE,  related_name='dono')
    data_requisito = models.DateTimeField()
    status = models.CharField(choices=STATUS_CHOICES,max_length=1)
    objeto_solicitado = models.ForeignKey(Objeto, on_delete=models.CASCADE)
