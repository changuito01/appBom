from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm
from .forms import RegistroUsuarioForm, HerramientaForm 
from personal.models import UsuarioPersonalizado
from django.contrib.auth import login as auth_login
from .models import Inventario, Bombero
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


def index(request):
    return render(request, 'index.html')


def inventario(request):
    inventario_data = Inventario.objects.all()
    return render(request, 'componentes/inventario.html', {'inventario_data': inventario_data})


def historial(request):
    inventario_data = Inventario.objects.all()
    return render(request, 'componentes/historial.html', {'inventario_data': inventario_data})


def eliminar_herramienta(request, pk):
    herramienta = get_object_or_404(Inventario, pk=pk)
    herramienta.delete()
    return redirect('inventario')


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        next_url = self.request.POST.get('next', None)
        
        if next_url:
            return redirect(next_url)
        else:
            return response

    def get_success_url(self):
        return reverse_lazy('inventario')


def actualizar_herramienta(request, pk):
    herramienta = get_object_or_404(Inventario, pk=pk)

    if request.method == 'POST':
        form = HerramientaForm(request.POST, instance=herramienta)
        if form.is_valid():
            form.save()
            return redirect('inventario')
    else:
        form = HerramientaForm(instance=herramienta)

    return render(request, 'componentes/actualizar.html', {'form': form})


def registrar_herramienta(request):
    if request.method == 'POST':
        form = HerramientaForm(request.POST)
        if form.is_valid():
            herramienta = form.save(commit=False)
            herramienta.save()
            return redirect('inventario') 
    else:
        form = HerramientaForm()

    return render(request, 'componentes/registrar_herramienta.html', {'form': form})


def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registration/registro.html', {'form': form})