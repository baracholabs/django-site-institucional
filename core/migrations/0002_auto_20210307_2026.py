# Generated by Django 3.1.7 on 2021-03-07 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamrole',
            name='criados',
        ),
        migrations.RemoveField(
            model_name='teamrole',
            name='modificado',
        ),
        migrations.AddField(
            model_name='service',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo?'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo?'),
        ),
    ]
