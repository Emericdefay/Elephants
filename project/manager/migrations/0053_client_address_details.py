# Generated by Django 4.0.3 on 2022-04-30 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0052_remove_client_description_remove_command_reduction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='address_details',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Details'),
        ),
    ]
