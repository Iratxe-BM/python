# Generated by Django 2.1.1 on 2018-09-02 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('submitter', models.CharField(max_length=10)),
                ('species', models.CharField(max_length=10)),
                ('breed', models.CharField(max_length=10, null=True)),
                ('description', models.TextField()),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('submission_date', models.DateTimeField()),
                ('age', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='vaccinations',
            field=models.ManyToManyField(blank=True, to='adoptions.Vaccine'),
        ),
    ]