# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_control', '0002_initial_app_control'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Function_controller',
            new_name='FunctionController',
        ),
    ]
