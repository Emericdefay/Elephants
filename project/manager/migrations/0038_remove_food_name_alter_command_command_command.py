# Generated by Django 4.0.3 on 2022-04-07 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0037_command_free_command_reduction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='name',
        ),
        migrations.AlterField(
            model_name='command',
            name='command_command',
            field=models.IntegerField(default=0, verbose_name=''),
        ),
    ]
