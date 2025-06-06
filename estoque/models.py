from django.db import models

class Ativo(models.Model):
    tipo = models.CharField(max_length=50)
    nome = models.CharField(max_length=100)
    numero_patrimonio = models.CharField(max_length=50, unique=True)
    serial_number = models.CharField(max_length=100, blank=True)
    ram = models.CharField(max_length=50, blank=True)
    hd = models.CharField(max_length=50, blank=True)
    processador = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('disponível', 'Disponível'),
        ('em uso', 'Em uso'),
        ('manutenção', 'Manutenção'),
        ('descartado', 'Descartado'),
    ])
    data_aquisicao = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.nome} ({self.numero_patrimonio})"
