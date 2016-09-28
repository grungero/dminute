# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetingmanagement', '0011_auto_20150808_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elemento',
            name='titulo_elemento',
            field=models.CharField(max_length=200, verbose_name=b'Titulo'),
        ),
        migrations.AlterField(
            model_name='tema',
            name='titulo_tema',
            field=models.CharField(max_length=200),
        ),
    ]
