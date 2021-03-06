# Generated by Django 3.2.12 on 2022-04-22 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diak',
            old_name='felvettek_e',
            new_name='Atagozat',
        ),
        migrations.AddField(
            model_name='diak',
            name='Btagozat',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diak',
            name='Ctagozat',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diak',
            name='Dtagozat',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diak',
            name='Etagozat',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diak',
            name='Ftagozat',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diak',
            name='pontszam',
            field=models.IntegerField(default=1, ),
            preserve_default=False,
        ),
    ]
