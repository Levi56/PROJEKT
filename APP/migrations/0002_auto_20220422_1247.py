# Generated by Django 3.2.13 on 2022-04-22 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diak',
            name='Aosztaly',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diak',
            name='Bosztaly',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diak',
            name='Cosztaly',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diak',
            name='Dosztaly',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diak',
            name='Eosztaly',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diak',
            name='Fosztaly',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diak',
            name='nev',
            field=models.CharField(default=23, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diak',
            name='om',
            field=models.CharField(default=457, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diak',
            name='pontszam',
            field=models.IntegerField(default=43256, ),
            preserve_default=False,
        ),
    ]
