# Generated by Django 4.0.6 on 2022-08-26 19:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_book_instances_requested'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_instances',
            name='requested',
        ),
        migrations.AddField(
            model_name='req_user',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.book_instances'),
        ),
        migrations.AddField(
            model_name='req_user',
            name='req',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='book_instances',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='book_instances',
            name='recieved_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='req_user',
            name='req_date',
            field=models.DateTimeField(null=True),
        ),
    ]
