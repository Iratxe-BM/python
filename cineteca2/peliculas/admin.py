from django.contrib import admin
from .models import Pelicula
@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display=['titulo','director','actor_principal','actriz_principal']
