from django import forms
from .models import Juego, Usuario

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = '__all__'
        
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
