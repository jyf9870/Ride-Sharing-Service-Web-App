# Generated by Django 4.1.5 on 2023-02-03 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride_sharing_service', '0014_alter_ride_requested_vehicle_type_alter_ride_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='requested_vehicle_type',
            field=models.CharField(blank=True, choices=[('Sports Car', 'Sports Car'), ('Convertible', 'Convertible'), ('Minivan', 'Minivan'), ('Coupe', 'Coupe'), ('SUV', 'Sport Utility Vehicle'), ('Hatchback', 'Hatchback'), ('Truck', 'Pickup Truck'), ('Crossover', 'Crossover'), ('Sedan', 'Sedan')], max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Confirmed', 'Confirmed'), ('Complete', 'Complete')], default='Open', max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='vehicle_type',
            field=models.CharField(blank=True, choices=[('Sports Car', 'Sports Car'), ('Convertible', 'Convertible'), ('Minivan', 'Minivan'), ('Coupe', 'Coupe'), ('SUV', 'Sport Utility Vehicle'), ('Hatchback', 'Hatchback'), ('Truck', 'Pickup Truck'), ('Crossover', 'Crossover'), ('Sedan', 'Sedan')], max_length=64, null=True),
        ),
    ]