# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0007_seed_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='seed',
            name='intro2',
            field=models.TextField(blank=True),
        ),
    ]
