# Generated by Django 3.0.7 on 2020-12-13 06:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20201213_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 12, 13, 6, 33, 17, 187169)),
        ),
        migrations.AlterField(
            model_name='book',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 12, 13, 6, 33, 17, 187188)),
        ),
        migrations.AlterField(
            model_name='bus',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 12, 13, 6, 33, 17, 186147)),
        ),
        migrations.AlterField(
            model_name='bus',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 12, 13, 6, 33, 17, 186184)),
        ),
    ]