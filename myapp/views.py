from django.shortcuts import render

# Create your views here.

def index(request):
    context = { 'mensaje' : 'Está usando Django, excelente!'}
    return render(request, 'myapp/index.html', context)