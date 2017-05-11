from django.contrib import admin
from polls.models import Opcion, Pregunta

class OpcionInline(admin.TabularInline):
    model = Opcion
    extra = 3

class PreguntaAdmin(admin.ModelAdmin):
    fieldsets = [
    (None, {'fields': ['texto_pregunta']}),('fecha', {'fields': ['fecha'],'classes': ['collapse']}),
    ]
    inlines = [OpcionInline]
    list_filter = ['fecha']
    search_fields = ["texto_pregunta"]

admin.site.register(Pregunta, PreguntaAdmin)
