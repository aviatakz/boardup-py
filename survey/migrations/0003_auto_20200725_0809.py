# Generated by Django 3.0.8 on 2020-07-25 08:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20200722_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 25, 8, 9, 40, 931360, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='survey',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 25, 8, 9, 40, 931307, tzinfo=utc)),
        ),
    ]
