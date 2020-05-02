# Generated by Django 3.0.4 on 2020-04-18 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0007_auto_20200418_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garden',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Garden Name'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/plants', verbose_name='Main Picture'),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagefile', models.ImageField(upload_to='images/plants/more', verbose_name='More Picture')),
                ('plant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='plant.Plant')),
            ],
        ),
    ]
