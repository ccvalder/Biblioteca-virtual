from django import forms
from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['usuario', 'libro', 'fecha_prestamo', 'fecha_devolucion']
        widgets = {
            'fecha_prestamo': forms.DateInput(attrs={'type': 'date'}),
            'fecha_devolucion': forms.DateInput(attrs={'type': 'date'}),
        }
