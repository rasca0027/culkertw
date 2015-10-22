# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('quote', models.CharField(max_length=60)),
                ('location', models.CharField(max_length=20, choices=[(b'N', b'north'), (b'M', b'middle'), (b'S', b'south'), (b'E', b'east'), (b'O', b'other')])),
                ('intro', models.TextField()),
                ('avatar', models.CharField(max_length=1000)),
                ('banner1', models.CharField(max_length=1000)),
                ('banner2', models.CharField(max_length=1000)),
                ('banner3', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=25)),
                ('duration', models.CharField(max_length=20)),
                ('people', models.IntegerField(default=1)),
                ('fee', models.IntegerField()),
                ('cancel', models.CharField(max_length=20, choices=[(b'flexible', b'flexible'), (b'strict', b'strict')])),
                ('short_descp', models.TextField()),
                ('cover_photo', models.CharField(max_length=1000)),
                ('paragraph1', models.TextField()),
                ('paragraph2', models.TextField()),
                ('paragraph3', models.TextField()),
                ('timetable', models.TextField()),
                ('note', models.TextField()),
                ('pic1', models.CharField(max_length=1000)),
                ('pic2', models.CharField(max_length=1000)),
                ('pic3', models.CharField(max_length=1000)),
                ('seed', models.ForeignKey(to='travel.Seed')),
            ],
        ),
    ]
