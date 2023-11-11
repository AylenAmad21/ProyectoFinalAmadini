from django.db import models
from django.contrib.auth.models import User

class Turno(models.Model):
    services_choices = [
        ('lavado Premium Basico', 'Lavado Premium Basico' ),
        ('lavado Premium Plus', 'Lavado Premium Plus'),
        ('lavado Premium Deluxe', 'Lavado Premium Deluxe'),
        ('pulido Vehicular', 'Pulido Vehicular'),
        ('pulido de Opticas','Pulido de Opticas'),
        ('polarizado','Polarizado'),
        ('wrapping Vehicular', 'Wrapping Vehicular'),
]
    date = models.DateField(max_length=100, default=None)
    time = models.TimeField(max_length=100, default=None)
    service = models.CharField(max_length=100, verbose_name='servicio', choices=services_choices, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return " Hola " + (self.user.username) +"!" + "Agendaste un turno el dia " + str(self.date) + "a las" + str(self.time) + " para el servicio " + self.service










