from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100, default="General")
    publicado = models.DateField()

    def __str__(self):
        return self.titulo


class Prestamo(models.Model):
    # En lugar de referirte directamente a Libro, usa una referencia como string
    libro = models.ForeignKey('Libro', on_delete=models.CASCADE, related_name='prestamos')
    usuario = models.CharField(max_length=100)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Préstamo: {self.libro.titulo} a {self.usuario}"
