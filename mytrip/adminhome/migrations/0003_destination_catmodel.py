# Generated by Django 5.0.3 on 2024-04-06 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminhome', '0002_locationmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination_catModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Destination_cat', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
