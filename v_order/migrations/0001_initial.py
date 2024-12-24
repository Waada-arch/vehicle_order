# Generated by Django 5.1.1 on 2024-12-03 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('aadhaar', models.CharField(blank=True, max_length=12, null=True)),
                ('license', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=100)),
                ('vehicle', models.CharField(max_length=50)),
                ('availability', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('age', models.IntegerField()),
                ('message', models.TextField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]
