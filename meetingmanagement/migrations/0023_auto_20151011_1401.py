# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetingmanagement', '0022_auto_20151011_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarea_kanban',
            name='elemento_dialogico',
        ),
        migrations.RemoveField(
            model_name='usuario_tarea',
            name='tarea',
        ),
        migrations.DeleteModel(
            name='Tarea_Kanban',
        ),
        migrations.RemoveField(
            model_name='usuario_tarea',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Usuario_Tarea',
        ),
    ]
