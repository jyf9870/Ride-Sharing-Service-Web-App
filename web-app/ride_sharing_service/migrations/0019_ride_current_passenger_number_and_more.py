# Generated by Django 4.1.5 on 2023-02-05 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride_sharing_service', '0018_alter_ride_requested_vehicle_type_alter_ride_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='current_passenger_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='requested_vehicle_type',
            field=models.CharField(blank=True, choices=[('Coupe', 'Coupe'), ('Hatchback', 'Hatchback'), ('SUV', 'Sport Utility Vehicle'), ('Minivan', 'Minivan'), ('Crossover', 'Crossover'), ('Sports Car', 'Sports Car'), ('Convertible', 'Convertible'), ('Sedan', 'Sedan'), ('Truck', 'Pickup Truck')], max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Complete', 'Complete'), ('Confirmed', 'Confirmed')], default='Open', max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='vehicle_type',
            field=models.CharField(blank=True, choices=[('Coupe', 'Coupe'), ('Hatchback', 'Hatchback'), ('SUV', 'Sport Utility Vehicle'), ('Minivan', 'Minivan'), ('Crossover', 'Crossover'), ('Sports Car', 'Sports Car'), ('Convertible', 'Convertible'), ('Sedan', 'Sedan'), ('Truck', 'Pickup Truck')], max_length=64, null=True),
        ),
    ]
