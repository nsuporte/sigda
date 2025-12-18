import os
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    name = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return f"{self.name}"
    
class Obra(models.Model):
    ESTADO = [
        ('Pendente', 'Pendente'),
        ('Aprovado', 'Aprovado'),
        ('Reprovado', 'Reprovado'),
    ]
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.CharField(max_length=10, choices=ESTADO, default='Pendente')
    ano_publicacao = models.IntegerField()
    resumo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.titulo} by {self.autor}"
    
class Arquivo(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='arquivos/obras/%Y/%m/%d/')
    enviado_em = models.DateTimeField(auto_now_add=True)
    
    def nomearquivo(self):
        return os.path.basename(self.arquivo.name)
