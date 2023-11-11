from django import forms
from .models import Turno

	
class TurnoForm(forms.ModelForm):
    date= forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Fecha')
    time= forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), label='Hora')
    class Meta:
        model = Turno
        fields = ['date', 'time', 'service']
        labels = {
            'date': 'Fecha',
            'time' : 'Hora',
            'service': 'Servicio',

        
        }
        




   