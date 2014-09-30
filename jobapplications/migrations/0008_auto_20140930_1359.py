# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapplications', '0007_blacklistedcompany'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blacklistedcompany',
            name='company',
        ),
        migrations.DeleteModel(
            name='BlacklistedCompany',
        ),
        migrations.RemoveField(
            model_name='company',
            name='added_date',
        ),
        migrations.AddField(
            model_name='company',
            name='is_blacklisted',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
    ]
