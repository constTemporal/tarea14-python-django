# Generated by Django 4.1.9 on 2023-05-23 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0021_alter_pelicula_portada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='portada',
            field=models.ImageField(upload_to='catalog/'),
        ),
    ]
