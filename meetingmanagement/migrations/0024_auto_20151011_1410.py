# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetingmanagement', '0023_auto_20151011_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='descripcion_proyecto',
            field=models.TextField(verbose_name=b'Descripci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='tema',
            name='descripcion_tema',
            field=models.TextField(verbose_name=b'Descripci\xc3\xb3n del Tema'),
        ),
    ]
