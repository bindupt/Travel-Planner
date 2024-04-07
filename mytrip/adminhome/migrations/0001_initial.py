# Generated by Django 5.0.3 on 2024-04-03 15:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State', models.CharField(max_length=20, null=True)),
                ('country', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adminhome.countrymodel')),
            ],
        ),
        migrations.CreateModel(
            name='DistrictModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('District', models.CharField(max_length=20, null=True)),
                ('Area', models.CharField(max_length=20, null=True)),
                ('Population', models.CharField(max_length=20, null=True)),
                ('Altitude', models.CharField(max_length=20, null=True)),
                ('Telcode', models.CharField(max_length=20, null=True)),
                ('Description', models.CharField(max_length=20, null=True)),
                ('Air', models.CharField(max_length=20, null=True)),
                ('Rail', models.CharField(max_length=20, null=True)),
                ('Road', models.CharField(max_length=20, null=True)),
                ('Backwarter', models.CharField(max_length=20, null=True)),
                ('state', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adminhome.statemodel')),
            ],
        ),
    ]