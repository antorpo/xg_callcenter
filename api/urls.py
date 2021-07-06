from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadenaList, name="cadena-list"),
    path('cadena-create/', views.cadenaCreate, name="cadena-create"),
    path('cadena-delete-all/', views.cadenaDeleteAll, name="cadena-delete-all"),
    path('historial/', views.historialPuntaje, name="historial")
]