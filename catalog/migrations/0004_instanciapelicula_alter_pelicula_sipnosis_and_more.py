# Generated by Django 4.1.9 on 2023-05-19 04:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_genero_pelicula_remove_book_premios_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstanciaPelicula',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Identificador unico para esta pelicula.', primary_key=True, serialize=False)),
                ('impresion', models.CharField(max_length=200)),
                ('desde', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='m', help_text='Book availability', max_length=1)),
            ],
            options={
                'ordering': ['desde'],
            },
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='sipnosis',
            field=models.TextField(help_text='Describe un poco sobre la peliculas sin mucho spoiler :)', max_length=1000),
        ),
        migrations.DeleteModel(
            name='BookInstance',
        ),
        migrations.AddField(
            model_name='instanciapelicula',
            name='pelicula',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.pelicula'),
        ),
    ]
