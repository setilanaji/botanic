# Generated by Django 3.0.4 on 2020-04-05 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0002_auto_20200405_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='botanic',
            name='address',
            field=models.CharField(blank=True, max_length=200, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='botanic',
            name='website',
            field=models.CharField(blank=True, max_length=100, verbose_name='Website'),
        ),
        migrations.AddField(
            model_name='plant',
            name='origin',
            field=models.CharField(blank=True, max_length=100, verbose_name='Origin'),
        ),
    ]
