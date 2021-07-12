# Generated by Django 3.2.5 on 2021-07-12 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netmon', '0005_device_dev_status_changed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert_desc', models.CharField(max_length=100)),
                ('alert_name', models.CharField(max_length=100)),
                ('alert_ip', models.CharField(max_length=16)),
                ('alert_type', models.CharField(max_length=100)),
            ],
        ),
    ]
