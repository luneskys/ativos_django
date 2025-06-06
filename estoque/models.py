from django.db import models

class Ativo(models.Model):
    nome = models.CharField(max_length=100)
    numero_patrimonio = models.CharField(max_length=50, unique=True)
    categoria = models.CharField(max_length=50)
    localizacao = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[
        ('disponível', 'Disponível'),
        ('em uso', 'Em uso'),
        ('manutenção', 'Manutenção'),
        ('descartado', 'Descartado'),
    ])
    data_aquisicao = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.numero_patrimonio})"
