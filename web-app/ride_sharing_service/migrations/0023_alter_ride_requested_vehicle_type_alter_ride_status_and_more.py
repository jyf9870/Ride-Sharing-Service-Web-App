# Generated by Django 4.1.5 on 2023-02-05 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride_sharing_service', '0022_alter_ride_requested_vehicle_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='requested_vehicle_type',
            field=models.CharField(blank=True, choices=[('Crossover', 'Crossover'), ('Minivan', 'Minivan'), ('Truck', 'Pickup Truck'), ('SUV', 'Sport Utility Vehicle'), ('Convertible', 'Convertible'), ('Coupe', 'Coupe'), ('Hatchback', 'Hatchback'), ('Sports Car', 'Sports Car'), ('Sedan', 'Sedan')], max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Completed', 'Completed'), ('Confirmed', 'Confirmed')], default='Open', max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='vehicle_type',
            field=models.CharField(blank=True, choices=[('Crossover', 'Crossover'), ('Minivan', 'Minivan'), ('Truck', 'Pickup Truck'), ('SUV', 'Sport Utility Vehicle'), ('Convertible', 'Convertible'), ('Coupe', 'Coupe'), ('Hatchback', 'Hatchback'), ('Sports Car', 'Sports Car'), ('Sedan', 'Sedan')], max_length=64, null=True),
        ),
    ]
