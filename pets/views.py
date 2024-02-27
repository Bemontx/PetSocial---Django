from django.shortcuts import render, redirect
from .forms import MascotaForm
from .models import Servicio

def agregar_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_mascota')  
    else:
        form = MascotaForm()
    return render(request, 'pets/agregar_mascota.html', {'form': form})

def ver_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'pets/ver_servicios.html', {'servicios': servicios})