# Generated by Django 3.0.5 on 2020-05-25 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0014_remove_order_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
