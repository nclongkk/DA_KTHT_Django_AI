# Generated by Django 3.2.9 on 2021-11-26 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timecheckin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=30)),
                ('user', models.CharField(max_length=30)),
                ('timeLate', models.IntegerField()),
                ('day', models.DateField()),
            ],
        ),
    ]
