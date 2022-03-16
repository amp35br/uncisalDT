from django.db import models


class assunto(models.Model):
    assunto = models.CharField(max_length=150)


class publico(models.Model):
    publico = models.CharField(max_length=50)
    nome = models.CharField(max_length=150)


class tipo(models.Model):
    tipo = models.CharField(max_length=50)
