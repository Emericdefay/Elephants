# Generated by Django 4.0.3 on 2022-04-03 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0031_remove_command_meals_command_evening_meals_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='order',
            field=models.IntegerField(default=1, verbose_name='Position de tournée'),
            preserve_default=False,
        ),
    ]
