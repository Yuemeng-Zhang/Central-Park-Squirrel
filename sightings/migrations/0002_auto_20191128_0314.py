# Generated by Django 2.2.7 on 2019-11-28 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='primary_flur_color',
            field=models.CharField(choices=[('Cinnamon', 'Cinnamon'), ('Black', 'Black'), ('Grey', 'Grey')], default='Grey', help_text='Primary flur color', max_length=30),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='shift',
            field=models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', help_text='shift', max_length=10),
        ),
    ]
