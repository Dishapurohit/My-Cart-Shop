# Generated by Django 3.0.5 on 2020-05-25 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0006_auto_20200525_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=''),
        ),
    ]
