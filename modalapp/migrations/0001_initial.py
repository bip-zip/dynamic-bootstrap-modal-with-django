# Generated by Django 4.2.9 on 2024-01-26 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingLot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('vehicle_capacity', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(choices=[('Bike', 'bike'), ('Car', 'car'), ('Scooter', 'scooter')], default='bike', max_length=12)),
                ('vehicle_number', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=30)),
                ('entry_time', models.DateTimeField(auto_now=True)),
                ('parkinglot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modalapp.parkinglot')),
            ],
        ),
    ]