# Generated by Django 4.1.5 on 2023-02-03 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride_sharing_service', '0010_alter_ride_requested_vehicle_type_alter_ride_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='requested_vehicle_type',
            field=models.CharField(blank=True, choices=[('Sports Car', 'Sports Car'), ('Truck', 'Pickup Truck'), ('Coupe', 'Coupe'), ('Hatchback', 'Hatchback'), ('Crossover', 'Crossover'), ('SUV', 'Sport Utility Vehicle'), ('Minivan', 'Minivan'), ('Convertible', 'Convertible'), ('Sedan', 'Sedan')], max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='vehicle_type',
            field=models.CharField(blank=True, choices=[('Sports Car', 'Sports Car'), ('Truck', 'Pickup Truck'), ('Coupe', 'Coupe'), ('Hatchback', 'Hatchback'), ('Crossover', 'Crossover'), ('SUV', 'Sport Utility Vehicle'), ('Minivan', 'Minivan'), ('Convertible', 'Convertible'), ('Sedan', 'Sedan')], max_length=64, null=True),
        ),
    ]
