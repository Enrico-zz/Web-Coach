from django.contrib import admin
from .models import Mentorados, Navigators,DisponibilidadeHorarios, Reuniao

# Register your models here.

admin.site.register(Mentorados)
admin.site.register(Navigators)
admin.site.register(DisponibilidadeHorarios)
admin.site.register(Reuniao)