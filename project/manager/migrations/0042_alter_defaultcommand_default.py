# Generated by Django 4.0.3 on 2022-04-18 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0041_alter_defaultcommand_default_alter_food_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defaultcommand',
            name='default',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.food', verbose_name='Plats réguliers'),
        ),
    ]
