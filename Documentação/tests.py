from django.test import TestCase
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

class Usuarios(TestCase):
    def setup(self):
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
        
    def test_login_usuario(self):
        self.setup()
        user = authenticate(username='jacob', password='top_secret')
        self.assertIsNotNone(user)

    def test_usuario_nao_existe(self):
        user = authenticate(username='15', password='gfdg')
        self.assertIsNone(user)

    def test_login_user_correto_senha_incorreta(self):
        self.setup()
        user = authenticate(username='jacob', password='top')
        self.assertIsNone(user)

    def test_login_user_incorreto_senha_correta(self):
        self.setup()
        user = authenticate(username='jaco', password='top_secret')
        self.assertIsNone(user)

    def test_criacao_usuario_existente(self):
        self.setup()
        with self.assertRaises(Exception):
            self.user = User.objects.create_user(
                username='jacob', email='jacob@…', password='top_secret')

class Doacoes(TestCase):
    def setup(self):
        pass
    
    def test_cadastrar_item(self):
        pass

    def test_lista_itens_cadastrados(self):
        pass

    def test_fazer_pedido(self):
        pass

    def test_recusar_pedido(self):
        pass

    def test_aceitar_pedido(self):
        pass
    
    
