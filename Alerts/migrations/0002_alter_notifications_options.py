# Generated by Django 4.2.3 on 2023-07-07 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alerts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notifications',
            options={'verbose_name': 'Notification', 'verbose_name_plural': 'Notifications'},
        ),
    ]