from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.

def home(request):
    users = User.objects.all()
    messages.success(request, "Usuarios listados")
    return render(request, "home.html", {'users': users})

def registerUser(request):
    fullName = request.POST['fullName']
    dateBirth = request.POST['birthday']
    email = request.POST['email']
    profilePicture = request.FILES['profilePicture']

    if User.objects.filter(email=email).count():
        messages.success(request, "Direccion de email ya existe")
        return redirect('/')

    user = User.objects.create(
        fullName = fullName,
        dateBirth = dateBirth,
        email = email,
        profilePicture = profilePicture,    
    )

    messages.success(request, "Usuario registrado")
    return redirect('/')

def editUser(request, id):
    user = User.objects.get(id=id)
    return render(request, 'formEditUser.html', {'user': user})

def updateUser(request, id):
    fullName = request.POST['fullName']
    dateBirth = request.POST['birthday']
    email = request.POST['email']
    profilePicture = request.FILES['profilePicture']

    user = User.objects.get(id=id)

    user.fullName = fullName
    user.dateBirth = dateBirth
    user.email = email
    user.profilePicture = profilePicture

    user.save()

    messages.success(request, "Usuario actualizado")
    return redirect('/')

def deleteUser(request, id):
    user = User.objects.get(id=id)
    user.delete()

    messages.success(request, "Usuario eliminado")
    return redirect('/')