# Generated by Django 4.1.5 on 2023-02-04 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride_sharing_service', '0015_alter_ride_requested_vehicle_type_alter_ride_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='requested_vehicle_type',
            field=models.CharField(blank=True, choices=[('Hatchback', 'Hatchback'), ('Crossover', 'Crossover'), ('Sports Car', 'Sports Car'), ('Minivan', 'Minivan'), ('Convertible', 'Convertible'), ('Truck', 'Pickup Truck'), ('SUV', 'Sport Utility Vehicle'), ('Sedan', 'Sedan'), ('Coupe', 'Coupe')], max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='status',
            field=models.CharField(choices=[('Confirmed', 'Confirmed'), ('Open', 'Open'), ('Complete', 'Complete')], default='Open', max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='vehicle_type',
            field=models.CharField(blank=True, choices=[('Hatchback', 'Hatchback'), ('Crossover', 'Crossover'), ('Sports Car', 'Sports Car'), ('Minivan', 'Minivan'), ('Convertible', 'Convertible'), ('Truck', 'Pickup Truck'), ('SUV', 'Sport Utility Vehicle'), ('Sedan', 'Sedan'), ('Coupe', 'Coupe')], max_length=64, null=True),
        ),
    ]
