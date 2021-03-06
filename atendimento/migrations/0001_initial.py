# Generated by Django 3.2.12 on 2022-03-20 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='assunto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='publico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publico', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='atender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atendimento', models.DateField()),
                ('pessoa', models.CharField(max_length=150)),
                ('assunto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='atendimento.assunto')),
                ('publico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='atendimento.publico')),
                ('tipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='atendimento.tipo')),
            ],
        ),
    ]
