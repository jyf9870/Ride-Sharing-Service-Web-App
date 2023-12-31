# Generated by Django 4.1.5 on 2023-02-05 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride_sharing_service', '0019_ride_current_passenger_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='requested_vehicle_type',
            field=models.CharField(blank=True, choices=[('SUV', 'Sport Utility Vehicle'), ('Sports Car', 'Sports Car'), ('Convertible', 'Convertible'), ('Hatchback', 'Hatchback'), ('Crossover', 'Crossover'), ('Sedan', 'Sedan'), ('Minivan', 'Minivan'), ('Truck', 'Pickup Truck'), ('Coupe', 'Coupe')], max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Confirmed', 'Confirmed'), ('Open', 'Open')], default='Open', max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='vehicle_type',
            field=models.CharField(blank=True, choices=[('SUV', 'Sport Utility Vehicle'), ('Sports Car', 'Sports Car'), ('Convertible', 'Convertible'), ('Hatchback', 'Hatchback'), ('Crossover', 'Crossover'), ('Sedan', 'Sedan'), ('Minivan', 'Minivan'), ('Truck', 'Pickup Truck'), ('Coupe', 'Coupe')], max_length=64, null=True),
        ),
    ]
