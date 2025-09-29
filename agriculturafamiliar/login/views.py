from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm, EmailLoginForm

def login_view(request):
    if request.method == "POST":
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("index")
    else:
        form = EmailLoginForm()
    return render(request, "login/login.html", {"form": form})
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # loga automaticamente
            return redirect("index")
    else:
        form = CustomUserCreationForm()
    return render(request, "login/register.html", {"form": form})

