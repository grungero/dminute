# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetingmanagement', '0017_auto_20150911_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elemento',
            name='estado_elemento',
            field=models.CharField(max_length=255, verbose_name=b'Estado'),
        ),
        migrations.AlterField(
            model_name='tarea_kanban',
            name='nombre_tarea',
            field=models.CharField(max_length=255),
        ),
    ]
