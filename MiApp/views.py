from django.shortcuts import render

from MiApp.models import Amigos
# Create your views here.

def mostrar_amigos(request):

    a1 = Amigos(nombre='Juan Cruz', apellido='Flynn', edad=23, cumpleanios='1999-10-27') 
    a2 = Amigos(nombre='Catriel', apellido='Molina', edad=25, cumpleanios='1997-09-03')

    return render(request, 'MiApp/amigos.html', {'amigos':[a1, a2]})
