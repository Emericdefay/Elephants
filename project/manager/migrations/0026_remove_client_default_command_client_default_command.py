# Generated by Django 4.0.3 on 2022-03-28 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0025_remove_client_default_command_client_default_command'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='default_command',
        ),
        migrations.AddField(
            model_name='client',
            name='default_command',
            field=models.ManyToManyField(to='manager.defaultcommand'),
        ),
    ]
