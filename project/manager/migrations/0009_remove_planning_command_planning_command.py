# Generated by Django 4.0.3 on 2022-03-27 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_alter_client_options_alter_command_evening_command_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planning',
            name='command',
        ),
        migrations.AddField(
            model_name='planning',
            name='command',
            field=models.ManyToManyField(to='manager.command', verbose_name='Les commandes effectuées.'),
        ),
    ]
