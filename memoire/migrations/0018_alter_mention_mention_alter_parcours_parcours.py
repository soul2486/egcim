# Generated by Django 4.0.4 on 2022-06-02 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memoire', '0017_jury_encadreur_ind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mention',
            name='mention',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='parcours',
            name='parcours',
            field=models.CharField(max_length=50),
        ),
    ]
