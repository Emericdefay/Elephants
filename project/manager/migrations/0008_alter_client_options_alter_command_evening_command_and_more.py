# Generated by Django 4.0.3 on 2022-03-27 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_remove_client_circuit_client_circuit'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['circuit', 'last_name', 'first_name']},
        ),
        migrations.AlterField(
            model_name='command',
            name='evening_command',
            field=models.IntegerField(verbose_name='Commande Soir'),
        ),
        migrations.AlterField(
            model_name='command',
            name='morning_command',
            field=models.IntegerField(verbose_name='Commande Midi'),
        ),
    ]
