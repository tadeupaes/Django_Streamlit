# Generated by Django 5.1.7 on 2025-03-26 22:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('data_de_registro', models.DateField()),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadfun.departamentos')),
            ],
        ),
    ]
