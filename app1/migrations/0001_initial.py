# Generated by Django 3.2 on 2022-01-21 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resto_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('owname', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('pswrd', models.CharField(max_length=200)),
            ],
        ),
    ]
