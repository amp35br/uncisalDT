# Generated by Django 3.2.12 on 2022-03-17 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0004_auto_20220317_0100'),
    ]

    operations = [
        migrations.CreateModel(
            name='atender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atende', models.DateTimeField(auto_now_add=True)),
                ('assunto', models.ManyToManyField(to='atendimento.assunto')),
                ('publico', models.ManyToManyField(to='atendimento.publico')),
                ('tipo', models.ManyToManyField(to='atendimento.tipo')),
            ],
        ),
    ]
