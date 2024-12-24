# Generated by Django 5.1.1 on 2024-12-06 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v_order', '0004_alter_driver_aadhaar_alter_driver_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField()),
            ],
        ),
    ]