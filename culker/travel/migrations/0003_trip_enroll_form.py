# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_seed_feature'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='enroll_form',
            field=models.CharField(max_length=1000, blank=True),
        ),
    ]
