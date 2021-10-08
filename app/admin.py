from django.contrib import admin
from app.models import Produto

# Register your models here.
class Produtos(admin.ModelAdmin):
  # campos que devem ser exibidos
  list_display = ('id', 'nome', 'quantidade', 'valor')
  # campos que seram clicáveis
  list_display_links = ('id', 'nome')
  # campo de busca/filtro
  search_fields = ('nome',)

# registrando a model (model, classe)
admin.site.register(Produto, Produtos)