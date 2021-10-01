from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .forms import RegistroForm
from .models import Registro

"""
class ListView():
    model = Registro
    template_name = 'index.html'

    def get_queryset(self):
        return self.model.objects.all()
    
    def get_templates_names():
        return self.template_name

    def get(self,request,*args,**kwargs):
        return render(request,self.get_templates_name(),self.get_queryset())
"""