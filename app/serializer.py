# importando o serialize da ferramenta
from rest_framework import serializers
# importanto o nosso modelo
from app.models import Produto

# classe de serialização, com serializador de modelo
class ProdutoSerializer(serializers.ModelSerializer):
  # meta, onde configuramos o modelo e
  # os campos que queremos serializar
  class Meta:
    model = Produto
    fields = ['id','nome','quantidade', 'valor']