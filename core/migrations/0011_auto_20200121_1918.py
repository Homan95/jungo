# Generated by Django 3.0.2 on 2020-01-21 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200121_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bots',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Autor'),
        ),
    ]
