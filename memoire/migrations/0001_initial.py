# Generated by Django 4.0.4 on 2022-05-17 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='enseignant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('grade', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='entreprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('lieu', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('prenom', models.CharField(max_length=20)),
                ('matricule', models.CharField(max_length=20)),
                ('enseignant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memoire.enseignant')),
            ],
        ),
        migrations.CreateModel(
            name='mention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='soutenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salle', models.CharField(max_length=50)),
                ('jury', models.CharField(max_length=100)),
                ('note', models.FloatField(max_length=20)),
                ('mention', models.CharField(max_length=20)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField()),
                ('entreprise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memoire.entreprise')),
            ],
        ),
        migrations.CreateModel(
            name='parcours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('mention', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memoire.mention')),
            ],
        ),
        migrations.CreateModel(
            name='memoire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('mot_cle', models.CharField(max_length=100)),
                ('resume', models.CharField(max_length=10000)),
                ('memoire', models.CharField(max_length=100)),
                ('annee_academique', models.DateField()),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memoire.etudiant')),
                ('soutenance', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='memoire', to='memoire.soutenance')),
            ],
        ),
        migrations.AddField(
            model_name='etudiant',
            name='parcours',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memoire.parcours'),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memoire.stage'),
        ),
    ]
