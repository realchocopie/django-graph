# Generated by Django 3.2.6 on 2021-08-24 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='음식이름')),
                ('color', models.CharField(max_length=30, verbose_name='색깔')),
                ('value', models.IntegerField(verbose_name='투표')),
            ],
        ),
    ]
