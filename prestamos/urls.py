from django.urls import path
from . import views

app_name = 'prestamos'

urlpatterns = [
    path('', views.lista_prestamos, name='lista_prestamos'),
    path('crear/', views.crear_prestamo, name='crear_prestamo'),
    path('editar/<int:pk>/', views.actualizar_prestamo, name='actualizar_prestamo'),
    path('eliminar/<int:pk>/', views.eliminar_prestamo, name='eliminar_prestamo'),
]
