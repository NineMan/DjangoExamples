# Generated by Django 3.0.5 on 2020-04-11 08:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200411_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 11, 8, 27, 32, 236880, tzinfo=utc)),
        ),
    ]
