# Generated by Django 4.0.3 on 2022-03-27 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0014_day_eveningnumbercommand_month_morningnumbercommand_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='command',
            name='evening_command',
        ),
        migrations.AddField(
            model_name='command',
            name='evening_command',
            field=models.IntegerField(default=12, verbose_name='Commande Soir'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='command',
            name='morning_command',
        ),
        migrations.AddField(
            model_name='command',
            name='morning_command',
            field=models.IntegerField(default=1, verbose_name='Commande Midi'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='day',
            name='date',
            field=models.IntegerField(verbose_name='Jour'),
        ),
        migrations.AlterField(
            model_name='eveningnumbercommand',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='month',
            name='date',
            field=models.IntegerField(verbose_name='Mois'),
        ),
        migrations.AlterField(
            model_name='morningnumbercommand',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='year',
            name='date',
            field=models.IntegerField(verbose_name='Année'),
        ),
    ]
