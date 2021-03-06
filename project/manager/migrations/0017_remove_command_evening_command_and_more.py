# Generated by Django 4.0.3 on 2022-03-27 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0016_remove_command_evening_command_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='command',
            name='evening_command',
        ),
        migrations.AddField(
            model_name='command',
            name='evening_command',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='manager.eveningnumbercommand', verbose_name='Commande Soir'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='command',
            name='morning_command',
        ),
        migrations.AddField(
            model_name='command',
            name='morning_command',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='manager.morningnumbercommand', verbose_name='Commande Midi'),
            preserve_default=False,
        ),
    ]
