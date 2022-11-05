from django.urls import path

from MiApp.views import mostrar_amigos

urlpatterns = [
    path('', mostrar_amigos)
]