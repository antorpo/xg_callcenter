# Generated by Django 3.2 on 2021-07-06 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadena',
            name='secuencia',
            field=models.TextField(blank=True),
        ),
    ]
