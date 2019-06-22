from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Objeto

#Objeto -> tipo, nome, descrição, usuario_dono

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True, help_text="Exigido: Até 50 caracteres compostos por letras, dígitos e símbolos do tipo: @ . + - _ apenas", label="Nome de Usuário:")    
    first_name = forms.CharField(max_length=30, required=True, help_text='Exigido, máximo 30 caracteres.', label="Primeiro Nome:")
    last_name = forms.CharField(max_length=50, required=False, help_text='Opcional.', label="Sobrenome:")
    email = forms.EmailField(max_length=254, help_text='Informe um endereço de email válido.')
    password1 = forms.CharField(label="Senha:",
        widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmação da Senha:",
        widget=forms.PasswordInput,
        help_text="Coloque a mesma senha, novamente.")

    class Meta:
        model = User
        labels = {
        "username": "Nome de Usuário:"
        }
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class ProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', )


class ItemForm(forms.ModelForm):
    cidade = forms.CharField(max_length=30, required=True,)
    UF = forms.ChoiceField(required=True, choices = Objeto.UF_CHOICES,)
   


    class Meta:
        

        model = Objeto
        fields = ('nome', 'descrição', 'cidade', 'UF', 'tipo', 'imagem',)