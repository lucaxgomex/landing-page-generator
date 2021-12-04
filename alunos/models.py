from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Aluno(models.Model):
    # campos do aluno cadastrado
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    idade = models.IntegerField()  

    def __str__(self):
        return self.nome
