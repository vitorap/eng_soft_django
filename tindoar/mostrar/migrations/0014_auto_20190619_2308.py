# Generated by Django 2.2.1 on 2019-06-20 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mostrar', '0013_objeto_cidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objeto',
            name='cidade',
            field=models.CharField(default='Não especificada', max_length=50),
        ),
    ]
