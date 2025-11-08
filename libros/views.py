from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro
from .forms import LibroForm

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/lista_libros.html', {'libros': libros})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libros:lista_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/form_libro.html', {'form': form, 'accion': 'Crear'})

def actualizar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libros:lista_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/form_libro.html', {'form': form, 'accion': 'Actualizar'})

def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('libros:lista_libros')
    return render(request, 'libros/confirm_delete.html', {'obj': libro, 'tipo': 'Libro'})
