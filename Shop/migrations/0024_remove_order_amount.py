# Generated by Django 3.0.5 on 2020-05-28 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0023_order_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='amount',
        ),
    ]
