# Generated by Django 5.0.3 on 2024-04-03 15:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminhome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=20, null=True)),
                ('Description', models.CharField(max_length=20, null=True)),
                ('Hw_to_reach', models.CharField(max_length=20, null=True)),
                ('district', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adminhome.districtmodel')),
            ],
        ),
    ]
