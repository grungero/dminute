# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetingmanagement', '0015_auto_20150911_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tema',
            name='descripcion_tema',
            field=models.TextField(max_length=600, verbose_name=b'Descripci\xc3\xb3n del Tema'),
        ),
        migrations.AlterField(
            model_name='tema',
            name='titulo_tema',
            field=models.CharField(max_length=50),
        ),
    ]
