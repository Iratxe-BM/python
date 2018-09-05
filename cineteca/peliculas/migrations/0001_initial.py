# Generated by Django 2.1.1 on 2018-09-05 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=90)),
                ('director', models.CharField(max_length=90)),
                ('actor_principal', models.CharField(max_length=90)),
                ('genero', models.CharField(choices=[('C', 'Comedia'), ('D', 'Drama'), ('T', 'Terror')], max_length=1)),
                ('pais', models.CharField(max_length=90)),
                ('fecha_estreno', models.DateTimeField()),
                ('comentarios', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Premio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('premio', models.CharField(max_length=90)),
            ],
        ),
        migrations.AddField(
            model_name='pelicula',
            name='premios',
            field=models.ManyToManyField(blank=True, to='peliculas.Premio'),
        ),
    ]
