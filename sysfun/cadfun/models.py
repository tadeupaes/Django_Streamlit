from django.db import models

# Create your models here.
class Departamentos(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Funcionarios(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    data_de_registro = models.DateField()
    salario = models.DecimalField(max_digits=10,decimal_places=2)
    departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
