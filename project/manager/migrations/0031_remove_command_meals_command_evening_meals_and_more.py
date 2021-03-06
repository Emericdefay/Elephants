# Generated by Django 4.0.3 on 2022-04-02 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0030_client_cellphone_client_description_command_comment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='command',
            name='meals',
        ),
        migrations.AddField(
            model_name='command',
            name='evening_meals',
            field=models.ManyToManyField(related_name='evening_meals', to='manager.defaultcommand'),
        ),
        migrations.AddField(
            model_name='command',
            name='morning_meals',
            field=models.ManyToManyField(related_name='morning_meals', to='manager.defaultcommand'),
        ),
    ]
