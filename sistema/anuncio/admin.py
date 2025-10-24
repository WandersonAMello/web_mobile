from django.contrib import admin
from anuncio.models import Anuncio

@admin.register(Anuncio)
class AnuncioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'preco', 'data_criacao', 'ativo')
    search_fields = ('titulo', 'descricao')
    list_filter = ('ativo', 'data_criacao')
    ordering = ('-data_criacao',)
    list_per_page = 25
    fields = ('titulo', 'descricao', 'preco', 'veiculo', 'ativo')
    readonly_fields = ('data_criacao',)
    date_hierarchy = 'data_criacao'
    
    def veiculo_info(self, obj):
        return f'{obj.veiculo.marca} {obj.veiculo.modelo} ({obj.veiculo.ano})'
    veiculo_info.short_description = 'Veículo'
    readonly_fields = ('veiculo_info',)