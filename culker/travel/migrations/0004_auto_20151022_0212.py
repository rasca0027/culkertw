# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_trip_enroll_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='cancel',
            field=models.CharField(max_length=20, choices=[(b'flexible', b'\xe9\x9d\x88\xe6\xb4\xbb'), (b'strict', b'strict')]),
        ),
    ]
