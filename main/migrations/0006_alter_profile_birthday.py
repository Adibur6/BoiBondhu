# Generated by Django 4.0.6 on 2022-08-06 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_profile_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
