from django.contrib import admin
from veiculo.models import Veiculo

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'ano', 'cor', 'combustivel')
    search_fields = ('marca', 'modelo', 'ano')
    list_filter = ('marca', 'ano', 'combustivel')
    ordering = ('marca', 'modelo')
    list_per_page = 25
    
    def foto_preview(self, obj):
        if obj.foto:
            return f'<img src="{obj.foto.url}" width="100" height="75" />'
        return "No Image"
    foto_preview.short_description = 'Foto Preview'
    readonly_fields = ('foto_preview',)
    fields = ('marca', 'modelo', 'ano', 'cor', 'combustivel', 'foto', 'foto_preview')