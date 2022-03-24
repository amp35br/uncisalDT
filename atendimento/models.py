from django.db import models


class atender(models.Model):
    atendimento = models.DateField()
    publico = models.ForeignKey(
        "publico", on_delete=models.CASCADE, related_name='atendidos', null=True)
    pessoa = models.CharField(max_length=150)
    tipo = models.ForeignKey(
        "tipo", on_delete=models.CASCADE, related_name='atendidos', null=True)
    assunto = models.ForeignKey(
        "assunto", on_delete=models.CASCADE, related_name='atendidos', null=True)

    def __str__(self):
        return str(self.atendimento)


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
