# Generated by Django 3.0.5 on 2020-05-25 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0008_auto_20200525_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=''),
        ),
    ]