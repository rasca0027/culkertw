# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_auto_20151022_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='header1',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='header2',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='header3',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='cancel',
            field=models.CharField(max_length=20, choices=[(b'flexible', b'\xe9\x9d\x88\xe6\xb4\xbb'), (b'strict', b'\xe5\x9a\xb4\xe6\xa0\xbc')]),
        ),
    ]
