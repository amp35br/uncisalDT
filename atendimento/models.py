from django.db import models


class atender(models.Model):
    ocorrencia = models.DateTimeField(auto_now_add=True)
    atendimento = models.DateTimeField()
    publico = models.ForeignKey("publico", on_delete=models.CASCADE, null=True)
    pessoa = models.ForeignKey("pessoa", on_delete=models.CASCADE, null=True)
    tipo = models.ForeignKey("tipo", on_delete=models.CASCADE, null=True)
    assunto = models.ForeignKey("assunto", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.atendimento)


class pessoa(models.Model):
    pessoa = models.CharField(max_length=150)

    def __str__(self):
        return self.pessoa


class assunto(models.Model):
    assunto = models.CharField(max_length=150)

    def __str__(self):
        return self.assunto


class publico(models.Model):
    publico = models.CharField(max_length=50)

    def __str__(self):
        return self.publico


class tipo(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo
