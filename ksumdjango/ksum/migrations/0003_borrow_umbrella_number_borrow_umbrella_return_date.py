# Generated by Django 4.1 on 2022-09-03 15:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ksum', '0002_alter_user_student_number_borrow'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow',
            name='umbrella_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='borrow',
            name='umbrella_return_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
