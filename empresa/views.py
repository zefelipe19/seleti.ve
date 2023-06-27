from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def nova_empresa(request):
    template_name = 'nova_empresa.html'
    return render(request, template_name)
