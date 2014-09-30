# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapplications', '0003_auto_20140930_0823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='name',
        ),
    ]
