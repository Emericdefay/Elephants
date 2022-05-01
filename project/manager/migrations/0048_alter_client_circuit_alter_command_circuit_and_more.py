# Generated by Django 4.0.3 on 2022-04-20 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0047_alter_client_circuit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='circuit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manager.circuit'),
        ),
        migrations.AlterField(
            model_name='command',
            name='circuit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='manager.circuit'),
        ),
        migrations.AlterField(
            model_name='command',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.client'),
        ),
    ]