# Generated by Django 4.0.6 on 2022-08-19 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_book_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.book'),
        ),
    ]