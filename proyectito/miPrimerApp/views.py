from django.shortcuts import render, redirect
#agrgamos esta linea
from django.http import HttpResponse
#importamos modelos para usarlos
from .models import *

from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):

	return render(request, "index.html")


def registro(request):
	data = {
		'form': CustomUserCreationForm()
	}
	if request.method == "POST":
		formulario = CustomUserCreationForm(data=request.POST)
		if formulario.is_valid():
			usuario = formulario.save()
			usuario.save()
			user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
			login(request,user)
			messages.success(request, "Registro exitoso, inicia sesión")
			return redirect(to="miPrimerApp:index")
		data["form"] = formulario
	return render(request,'registration/registration.html', data)

def home(request):

	return render(request, "home.html")