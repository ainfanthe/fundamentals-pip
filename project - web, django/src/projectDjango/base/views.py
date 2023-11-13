from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Tarea
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

class logueo(LoginView):
    template_name = "base/login.html"
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('tareas')
    
class paginaRegistro(FormView):
    template_name = 'base/registro.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tareas')
    
    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(paginaRegistro, self).form_valid(form)    
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tareas')
        return super(paginaRegistro, self).get(*args, **kwargs)
    
class listaPendientes(LoginRequiredMixin, ListView):
    model = Tarea
    context_object_name = 'tareas'
    
    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        context['tareas'] = context['tareas'].filter(usuario=self.request.user)
        context['count'] = context['tareas'].filter(completo=False).count()
        
        valor_buscado = self.request.GET.get('box-buscar') or ''
        if valor_buscado:
            context['tareas'] = context['tareas'].filter(titulo__icontains=valor_buscado)
            context['valor_buscado'] = valor_buscado
        return context
        
    
class detalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    context_object_name = 'tarea'
    template_name = 'base/tarea.html'
    
class crearTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy('tareas')
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(crearTarea, self).form_valid(form)
    
class editarTarea(LoginRequiredMixin, UpdateView):
    model = Tarea
    fields = ['titulo', 'descripcion', 'completo']
    success_url = reverse_lazy('tareas')
    

class eliminarTarea(LoginRequiredMixin, DeleteView):
    model = Tarea
    context_object_name = 'tarea'
    success_url = reverse_lazy('tareas')