# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetingmanagement', '0013_auto_20150911_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elemento',
            name='descripcion_elemento',
            field=models.CharField(max_length=1000, verbose_name=b'Descripcion'),
        ),
        migrations.AlterField(
            model_name='elemento',
            name='titulo_elemento',
            field=models.CharField(max_length=200, verbose_name=b'Titulo'),
        ),
        migrations.AlterField(
            model_name='tema',
            name='descripcion_tema',
            field=models.TextField(verbose_name=b'Descripci\xc3\xb3n del Tema'),
        ),
        migrations.AlterField(
            model_name='tema',
            name='titulo_tema',
            field=models.CharField(max_length=200),
        ),
    ]
