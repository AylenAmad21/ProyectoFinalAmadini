from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Turno
from .forms import TurnoForm

def servicios(request):
    return render(request, "AppCarwash/servicios.html")

def inicio(request):
    return render(request, "AppCarwash/inicio.html")

def contacto(request):
    return render(request, "AppCarwash/contacto.html")


def nosotros(request):
    return render(request, "AppCarwash/nosotros.html")

def turnos(request):
    return render(request, "AppCarwash/turnos.html")


def blog(request):
    return render(request, "AppCarwash/blog.html")

def ubicacion(request):
    return render(request, "AppCarwash/ubicacion.html")

def team (request):
    return render(request, "AppCarwash/team.html")

def construccion(request):
    return render(request, "AppCarwash/construccion.html")



def agendado(request):
    turnos = Turno.objects.filter(user=request.user)
    return render(request, 'AppCarwash/agendado.html', {'turnos': turnos})


def signup(request):
    if request.method == 'GET':
        return render(request, 'registro.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('Login')
            except IntegrityError:
                return render(request, 'registro.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'registro.html', {"form": UserCreationForm, "error": "Passwords did not match."})


@login_required   
def agendar(request):
    if request.method == "GET":
        return render(request, 'agendar.html', {"form": TurnoForm})
    else:
        try:
            form = TurnoForm(request.POST)
            new_turno = form.save(commit=False)
            new_turno.user = request.user
            new_turno.save()
            return redirect('Agendado')
        except ValueError:
            return render(request, 'agendar.html', {"form": TurnoForm, "error": "Error al crear turno."})

@login_required
def signout(request):
    logout(request)
    return redirect('inicio')


def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('Agendar')


def delete(request, turno_id):
    turno = turnos (Turno, pk=turno_id, user=request.user)
    if request.method == 'POST':
        turno.delete()
        return redirect('Agendado')

def editar(request, service_id):
    if request.method == 'GET':
        turno = get_object_or_404(Turno, pk=service_id, user=request.user)
        form = TurnoForm(instance=turno)
        return render(request, 'editar.html', {'turno': turno, 'form': form})
    else:
        try:
            turno = get_object_or_404(Turno,pk=service_id, user=request.user)
            form = TurnoForm(request.POST, instance=turno)
            form.save()
            return redirect('Agendado')
        except ValueError:
            return render(request, 'editar.html', {'turno': turno, 'form': form, 'error': 'Error updating turn.'})
            










