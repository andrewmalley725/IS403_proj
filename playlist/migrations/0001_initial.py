# Generated by Django 4.1.2 on 2022-12-03 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SongName', models.CharField(max_length=30)),
                ('Artist', models.CharField(max_length=20)),
                ('Album', models.CharField(max_length=20)),
                ('YearReleased', models.IntegerField()),
            ],
        ),
    ]
