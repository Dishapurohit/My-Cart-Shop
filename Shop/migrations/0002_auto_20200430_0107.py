# Generated by Django 3.0.5 on 2020-04-29 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=' ', upload_to='Shop/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
