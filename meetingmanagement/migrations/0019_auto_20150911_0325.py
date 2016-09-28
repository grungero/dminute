# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetingmanagement', '0018_auto_20150911_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tema',
            name='descripcion_tema',
            field=models.TextField(max_length=2000, verbose_name=b'Descripci\xc3\xb3n del Tema'),
        ),
    ]
