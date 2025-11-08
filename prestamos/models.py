from django.db import models
from libros.models import Libro

class Prestamo(models.Model):
    usuario = models.CharField(max_length=100)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='prestamos_prestamo')
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()

    def __str__(self):
        return f"{self.usuario} - {self.libro.titulo}"
