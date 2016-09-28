# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetingmanagement', '0020_auto_20150911_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elemento',
            name='descripcion_elemento',
            field=models.CharField(max_length=1200, verbose_name=b'Descripcion'),
        ),
        migrations.AlterField(
            model_name='elemento',
            name='titulo_elemento',
            field=models.CharField(max_length=100, verbose_name=b'Titulo'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='descripcion_proyecto',
            field=models.TextField(max_length=1200, verbose_name=b'Descripci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='nombre_proyecto',
            field=models.CharField(max_length=100, verbose_name=b'Nombre Proyecto'),
        ),
        migrations.AlterField(
            model_name='tema',
            name='descripcion_tema',
            field=models.TextField(max_length=1200, verbose_name=b'Descripci\xc3\xb3n del Tema'),
        ),
    ]
