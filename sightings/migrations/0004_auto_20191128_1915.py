# Generated by Django 2.2.7 on 2019-11-28 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0003_auto_20191128_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='primary_flur_color',
            field=models.CharField(choices=[('Black', 'Black'), ('Cinnamon', 'Cinnamon'), ('Grey', 'Grey')], default='Grey', help_text='Primary flur color', max_length=30),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='shift',
            field=models.CharField(choices=[('PM', 'PM'), ('AM', 'AM')], default='AM', help_text='shift', max_length=10),
        ),
    ]
