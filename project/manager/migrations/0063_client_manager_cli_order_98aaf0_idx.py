# Generated by Django 4.0.3 on 2022-05-03 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0062_alter_client_options'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='client',
            index=models.Index(fields=['order'], name='manager_cli_order_98aaf0_idx'),
        ),
    ]