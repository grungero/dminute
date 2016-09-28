# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetingmanagement', '0014_auto_20150911_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elemento',
            name='descripcion_elemento',
            field=models.CharField(max_length=600, verbose_name=b'Descripcion'),
        ),
        migrations.AlterField(
            model_name='elemento',
            name='titulo_elemento',
            field=models.CharField(max_length=50, verbose_name=b'Titulo'),
        ),
    ]
