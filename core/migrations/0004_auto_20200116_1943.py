# Generated by Django 3.0.2 on 2020-01-16 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_feeed_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeed',
            name='created',
            field=models.DateTimeField(default='1111-11-11 11:11'),
        ),
    ]
