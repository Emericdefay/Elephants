# Generated by Django 4.0.3 on 2022-04-10 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0039_alter_client_cellphone_alter_client_client_command_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='command',
            name='circuit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='manager.circuit'),
            preserve_default=False,
        ),
    ]
