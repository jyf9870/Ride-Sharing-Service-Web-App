# Generated by Django 4.1.5 on 2023-02-05 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride_sharing_service', '0021_alter_ride_requested_vehicle_type_alter_ride_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='requested_vehicle_type',
            field=models.CharField(blank=True, choices=[('Truck', 'Pickup Truck'), ('Crossover', 'Crossover'), ('Convertible', 'Convertible'), ('Sports Car', 'Sports Car'), ('Minivan', 'Minivan'), ('Coupe', 'Coupe'), ('SUV', 'Sport Utility Vehicle'), ('Sedan', 'Sedan'), ('Hatchback', 'Hatchback')], max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='vehicle_type',
            field=models.CharField(blank=True, choices=[('Truck', 'Pickup Truck'), ('Crossover', 'Crossover'), ('Convertible', 'Convertible'), ('Sports Car', 'Sports Car'), ('Minivan', 'Minivan'), ('Coupe', 'Coupe'), ('SUV', 'Sport Utility Vehicle'), ('Sedan', 'Sedan'), ('Hatchback', 'Hatchback')], max_length=64, null=True),
        ),
    ]