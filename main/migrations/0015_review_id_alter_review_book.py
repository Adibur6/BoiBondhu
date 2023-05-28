# Generated by Django 4.0.6 on 2022-08-19 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_review_id_alter_review_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='id',
            field=models.BigAutoField(auto_created=True, default=4, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.book'),
        ),
    ]
