# Generated by Django 4.0.4 on 2022-06-02 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memoire', '0016_encadreur_examinateur_president_jury_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jury',
            name='encadreur_ind',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
