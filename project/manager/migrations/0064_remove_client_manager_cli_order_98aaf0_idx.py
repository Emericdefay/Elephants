# Generated by Django 4.0.3 on 2022-05-03 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0063_client_manager_cli_order_98aaf0_idx'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='client',
            name='manager_cli_order_98aaf0_idx',
        ),
    ]
