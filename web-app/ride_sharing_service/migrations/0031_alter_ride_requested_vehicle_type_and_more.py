# Generated by Django 4.1.5 on 2023-02-06 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride_sharing_service', '0030_alter_ride_requested_vehicle_type_alter_ride_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='requested_vehicle_type',
            field=models.CharField(blank=True, choices=[('Minivan', 'Minivan'), ('Hatchback', 'Hatchback'), ('Coupe', 'Coupe'), ('Sedan', 'Sedan'), ('Crossover', 'Crossover'), ('Convertible', 'Convertible'), ('Truck', 'Pickup Truck'), ('Sports Car', 'Sports Car'), ('SUV', 'Sport Utility Vehicle')], default='', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='vehicle_type',
            field=models.CharField(blank=True, choices=[('Minivan', 'Minivan'), ('Hatchback', 'Hatchback'), ('Coupe', 'Coupe'), ('Sedan', 'Sedan'), ('Crossover', 'Crossover'), ('Convertible', 'Convertible'), ('Truck', 'Pickup Truck'), ('Sports Car', 'Sports Car'), ('SUV', 'Sport Utility Vehicle')], max_length=64, null=True),
        ),
    ]