from django.db import models

class Perfil(models.Model):

    nome = models.CharField(max_length=100)
    biografia = models.TextField()
    objetivo = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='perfil/', null=True, blank=True)
    curriculo = models.FileField(upload_to='curriculos/', null=True, blank=True)

    def __str__(self):
        return self.nome


class Experiencia(models.Model):
    empresa = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    historia = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField(blank=True, null=True)

    def __str__ (self):
        return f'{self.cargo}-{self.empresa}'
    
class Projeto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='projetos/')
    tecnologias = models.CharField(max_length=100)
    link_repositorio = models.URLField(blank=True)
    ordem = models.IntegerField(default=0)
    link_site = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.titulo

    


