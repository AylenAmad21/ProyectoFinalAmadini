from django.urls import path
from AppCarwash.views import *


urlpatterns = [
    path('servicios/', servicios, name= 'Servicios'),
    path('inicio/', inicio, name='Inicio'),
    path('contacto/', contacto, name='Contacto'),
    path('nosotros/', nosotros, name= 'Nosotros'),
    path('turnos/', turnos, name='Turnos'),
    path('blog/', blog, name='Blog'),
    path('ubicacion/', ubicacion, name='Ubicacion'),
    path('team/', team, name= 'Equipo'),
    path('login/', signin, name='Login'),
    path('registro/', signup, name='Registro'),
    path('construccion/', construccion, name='Construccion'),
    path('logout/', signout,name='Logout'),
    path('agendar/', agendar, name='Agendar'),
    path('agendado/', agendado, name='Agendado'),
    path('eliminar/<int:turno_id>/', delete, name='Eliminar'),
    path('editar/', editar, name= 'Editar'),


    ]
