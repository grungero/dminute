# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetingmanagement', '0012_auto_20150823_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elemento',
            name='titulo_elemento',
            field=models.CharField(max_length=50, verbose_name=b'Titulo'),
        ),
        migrations.AlterField(
            model_name='tema',
            name='descripcion_tema',
            field=models.TextField(max_length=10000, verbose_name=b'Descripci\xc3\xb3n del Tema'),
        ),
        migrations.AlterField(
            model_name='tema',
            name='titulo_tema',
            field=models.CharField(max_length=50),
        ),
    ]
