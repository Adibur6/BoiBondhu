# Generated by Django 4.0.6 on 2022-08-23 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_review_id_alter_review_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_instances',
            name='category',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
