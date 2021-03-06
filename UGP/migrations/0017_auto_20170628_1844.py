# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UGP', '0016_eukaryotestablenew1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eukaryotestablenew1',
            name='Chromosome',
            field=models.TextField(blank=True, default=b'-', null=True),
        ),
        migrations.AlterField(
            model_name='eukaryotestablenew1',
            name='Strand',
            field=models.TextField(blank=True, default=b'-', null=True),
        ),
        migrations.AlterField(
            model_name='eukaryotestablenew1',
            name='UpstreamATG',
            field=models.TextField(blank=True, default=b'-', null=True),
        ),
    ]
