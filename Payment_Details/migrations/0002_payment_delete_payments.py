# Generated by Django 4.2.3 on 2023-07-07 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Payment_Details', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
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
        migrations.DeleteModel(
            name='Payments',
        ),
    ]
