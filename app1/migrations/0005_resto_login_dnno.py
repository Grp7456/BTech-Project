# Generated by Django 3.2 on 2022-01-22 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_stock_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='resto_login',
            name='Dnno',
            field=models.IntegerField(default=0),
        ),
    ]