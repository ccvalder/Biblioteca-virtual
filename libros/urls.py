from django.urls import path
from . import views

app_name = 'libros'

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('crear/', views.crear_libro, name='crear_libro'),
    path('editar/<int:pk>/', views.actualizar_libro, name='actualizar_libro'),
    path('eliminar/<int:pk>/', views.eliminar_libro, name='eliminar_libro'),
]
