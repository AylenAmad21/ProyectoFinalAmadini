from django.contrib import admin
from .models import Turno
# Register your models here.

class TurnoAdmin(admin.ModelAdmin):
    list_display = ['date','time','service','user_id']
    search_fields = ['date','time','service','user_id']
    list_filter = ['date','time','service','user_id']


admin.site.register(Turno, TurnoAdmin)

