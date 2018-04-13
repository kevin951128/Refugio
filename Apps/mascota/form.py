from django import forms
from Apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota

        fields = [
            'Nombre',
            'Sexo',
            'Edad_Aproximada',
            'Fecha_Rescate',
            'Persona',
            'Vacuna',
        ]

        labels = {
            'Nombre': 'Nombre',
            'Sexo': 'Sexo',
            'Edad_Aproximada': 'Edad aproximada',
            'Fecha_Rescate': 'Fecha de rescate',
            'Persona': 'Adoptante',
            'Vacuna': 'Vacunas',
        }

        widgets = {
            'Nombre': forms.TextInput(attrs={'class':'form-control'}),
            'Sexo': forms.TextInput(attrs={'class':'form-control'}),
            'Edad_Aproximada':forms.TextInput(attrs={'class':'form-control'}),
            'Fecha_Rescate': forms.TextInput(attrs={'class':'form-control'}),
            'Persona':forms.Select(attrs={'class':'form-control'}),
            'Vacuna':forms.CheckboxSelectMultiple(),
        }