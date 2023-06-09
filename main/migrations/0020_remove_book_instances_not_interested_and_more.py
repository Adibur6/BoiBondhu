# Generated by Django 4.0.6 on 2022-08-26 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0019_alter_book_instances_not_interested'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_instances',
            name='not_interested',
        ),
        migrations.AddField(
            model_name='profile',
            name='coin_bonus',
            field=models.IntegerField(default=15),
        ),
        migrations.AlterField(
            model_name='book_instances',
            name='details',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.CreateModel(
            name='interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest_value', models.IntegerField(default=0, null=True)),
                ('book_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.book_instances')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
