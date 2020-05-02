# Generated by Django 3.0.4 on 2020-04-05 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0004_auto_20200405_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garden',
            name='botanic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='plant.Botanic'),
        ),
        migrations.AlterUniqueTogether(
            name='garden',
            unique_together=set(),
        ),
    ]
