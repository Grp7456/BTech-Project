# Generated by Django 3.2 on 2022-01-21 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_donor_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resid', models.CharField(max_length=200)),
                ('fname', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('stock', models.CharField(max_length=200)),
            ],
        ),
    ]
