# Generated by Django 5.1.1 on 2024-12-03 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v_order', '0003_alter_driver_aadhaar_alter_driver_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='aadhaar',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='driver',
            name='phone',
            field=models.IntegerField(),
        ),
    ]