# Generated by Django 4.0.4 on 2022-05-21 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memoire', '0009_soutenance_type_sout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memoire',
            name='resume',
            field=models.CharField(max_length=255),
        ),
    ]
