# Generated by Django 3.0.4 on 2020-06-05 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20200605_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='unique',
            field=models.UUIDField(default='1852c63687ce404da074b3aa364266a3', unique=True),
        ),
    ]
