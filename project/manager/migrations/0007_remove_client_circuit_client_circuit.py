# Generated by Django 4.0.3 on 2022-03-27 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_alter_client_options_client_circuit_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='circuit',
        ),
        migrations.AddField(
            model_name='client',
            name='circuit',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.PROTECT, to='manager.circuit'),
            preserve_default=False,
        ),
    ]
