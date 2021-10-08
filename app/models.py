from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=30)
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=19, decimal_places=2)

    def __str__(self):
        return self.nome
