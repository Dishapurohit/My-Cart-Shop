# Generated by Django 3.0.5 on 2020-05-25 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0011_auto_20200525_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='amount',
        ),
    ]
