# Generated by Django 4.2.1 on 2023-06-20 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt', models.TextField()),
                ('amount', models.FloatField()),
                ('payment_option', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('status', models.CharField(max_length=20)),
                ('order', models.TextField()),
            ],
        ),
    ]
