# Generated by Django 4.0.6 on 2022-09-08 10:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ksum', '0005_remove_user_student_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrow',
            name='room',
        ),
        migrations.RemoveField(
            model_name='borrow',
            name='umbrella_return_date',
        ),
        migrations.AddField(
            model_name='borrow',
            name='borrowed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='borrow',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2022, 9, 8, 19, 35, 57, 924811)),
        ),
    ]
