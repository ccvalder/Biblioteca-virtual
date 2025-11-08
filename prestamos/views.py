from django.shortcuts import render, get_object_or_404, redirect
from .models import Prestamo
from .forms import PrestamoForm

def lista_prestamos(request):
    prestamos = Prestamo.objects.select_related('libro').all()
    return render(request, 'prestamos/lista_prestamos.html', {'prestamos': prestamos})

def crear_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prestamos:lista_prestamos')
    else:
        form = PrestamoForm()
    return render(request, 'prestamos/form_prestamo.html', {'form': form, 'accion': 'Crear'})

def actualizar_prestamo(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    if request.method == 'POST':
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            return redirect('prestamos:lista_prestamos')
    else:
        form = PrestamoForm(instance=prestamo)
    return render(request, 'prestamos/form_prestamo.html', {'form': form, 'accion': 'Actualizar'})

def eliminar_prestamo(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    if request.method == 'POST':
        prestamo.delete()
        return redirect('prestamos:lista_prestamos')
    return render(request, 'prestamos/confirm_delete.html', {'obj': prestamo, 'tipo': 'Préstamo'})
