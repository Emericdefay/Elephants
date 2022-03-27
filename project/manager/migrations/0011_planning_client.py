# Generated by Django 4.0.3 on 2022-03-27 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0010_planning_month_date_planning_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='planning',
            name='client',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.PROTECT, to='manager.client'),
            preserve_default=False,
        ),
    ]
