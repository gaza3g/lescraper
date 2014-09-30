# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapplications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlacklistedCompany',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('is_blacklisted', models.NullBooleanField()),
                ('added_date', models.DateField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('added_date', models.DateField(verbose_name='date added')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blacklistedcompany',
            name='company',
            field=models.ForeignKey(to='jobapplications.Company'),
            preserve_default=True,
        ),
    ]
