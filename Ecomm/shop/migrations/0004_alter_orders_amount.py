# Generated by Django 4.2.2 on 2023-10-10 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_orders_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
