# Generated by Django 3.2.5 on 2021-07-12 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netmon', '0009_alter_device_dev_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='dev_latency',
            field=models.DecimalField(decimal_places=40, default='0.0', max_digits=40),
        ),
        migrations.AddField(
            model_name='device',
            name='dev_latency_count',
            field=models.IntegerField(default='0', max_length=4),
        ),
    ]