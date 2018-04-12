from django.contrib import admin

from Apps.mascota.models import Vacuna, Mascota


# Register your models here.

admin.site.register(Vacuna)
admin.site.register(Mascota)