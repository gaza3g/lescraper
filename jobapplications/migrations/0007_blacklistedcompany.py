# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapplications', '0006_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlacklistedCompany',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_blacklisted', models.NullBooleanField()),
                ('added_date', models.DateField(max_length=255)),
                ('company', models.ForeignKey(to='jobapplications.Company')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
