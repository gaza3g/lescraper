# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapplications', '0002_auto_20140930_0814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blacklistedcompany',
            name='company',
        ),
        migrations.DeleteModel(
            name='BlacklistedCompany',
        ),
    ]
