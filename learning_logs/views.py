from django.shortcuts import render

# Create your views here.
def index(request):
    """Página principal do Learning Log"""
    return render(request, 'learning_logs/index.html')