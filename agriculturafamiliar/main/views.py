from django.contrib.auth.decorators import login_required 
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, "main/index.html")

@login_required
def depoislogin(request):
    user = User.objects.get()
    context = {'user': user}
    return render(request, "main/pagina.html", context)