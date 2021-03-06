# Generated by Django 2.2.7 on 2019-11-27 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('unique_squirrel_id', models.CharField(help_text='Unique Squirrel ID', max_length=50)),
                ('shift', models.CharField(choices=[('PM', 'PM'), ('AM', 'AM')], default='AM', help_text='shift', max_length=10)),
                ('date', models.DateField(help_text='Date')),
                ('age', models.IntegerField()),
                ('primary_flur_color', models.CharField(choices=[('Black', 'Black'), ('Grey', 'Grey'), ('Cinnamon', 'Cinnamon')], default='Grey', help_text='Primary flur color', max_length=30)),
                ('location', models.CharField(choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], default='Above Ground', help_text='location', max_length=50)),
                ('specific_location', models.CharField(help_text='Specific location', max_length=100)),
                ('running', models.BooleanField(help_text='Squirrel was seen running')),
                ('chasing', models.BooleanField(help_text='Squirrel was seen chasing another squirrel')),
                ('climbing', models.BooleanField(help_text='Squirrel was seen climbing')),
                ('eating', models.BooleanField(help_text='Squirrel was seen eating')),
                ('foraging', models.BooleanField(help_text='Squirrel was seen foraging for food')),
                ('other_activities', models.CharField(help_text='Other activities', max_length=100)),
                ('kuks', models.BooleanField(help_text='Squirrel was heard kukking')),
                ('quaas', models.BooleanField(help_text='Squirrel was heard quaaing')),
                ('moans', models.BooleanField(help_text='Squirrel was heard moaning')),
                ('tail_flags', models.BooleanField(help_text='Squirrel was seen flagging its tail')),
                ('tail_twitches', models.BooleanField(help_text='Squirrel was seeen twitching its tail')),
                ('approaches', models.BooleanField(help_text='Squirrel was seen approaching human, seeking food')),
                ('indifferent', models.BooleanField(help_text='Squirrel was indifferent to human presence')),
                ('runs_from', models.BooleanField(help_text='Squirrel was seen running from humans')),
            ],
        ),
    ]
