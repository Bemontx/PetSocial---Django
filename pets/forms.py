from django import forms
from .models import Mascota

class MascotaForm(forms.ModelForm):
    foto = forms.ImageField(required=False)  

    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'raza', 'propietario', 'foto']