# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_auto_20151022_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seed',
            name='banner3',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='seed',
            name='location',
            field=models.CharField(max_length=20, choices=[(b'north', b'\xe5\x8c\x97\xe9\x83\xa8'), (b'middle', b'\xe4\xb8\xad\xe9\x83\xa8'), (b'south', b'\xe5\x8d\x97\xe9\x83\xa8'), (b'east', b'\xe6\x9d\xb1\xe9\x83\xa8'), (b'others', b'\xe5\x85\xb6\xe4\xbb\x96')]),
        ),
        migrations.AlterField(
            model_name='trip',
            name='fee',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='paragraph2',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='paragraph3',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='pic2',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='pic3',
            field=models.CharField(max_length=1000, blank=True),
        ),
    ]
