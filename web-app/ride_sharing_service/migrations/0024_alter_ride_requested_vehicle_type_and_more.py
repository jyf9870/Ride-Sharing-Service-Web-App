# Generated by Django 4.1.5 on 2023-02-06 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride_sharing_service', '0023_alter_ride_requested_vehicle_type_alter_ride_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='requested_vehicle_type',
            field=models.CharField(blank=True, choices=[('Coupe', 'Coupe'), ('Crossover', 'Crossover'), ('Convertible', 'Convertible'), ('Truck', 'Pickup Truck'), ('Minivan', 'Minivan'), ('Hatchback', 'Hatchback'), ('SUV', 'Sport Utility Vehicle'), ('Sedan', 'Sedan'), ('Sports Car', 'Sports Car')], default='', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='special_request',
            field=models.CharField(blank=True, default='', max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='vehicle_type',
            field=models.CharField(blank=True, choices=[('Coupe', 'Coupe'), ('Crossover', 'Crossover'), ('Convertible', 'Convertible'), ('Truck', 'Pickup Truck'), ('Minivan', 'Minivan'), ('Hatchback', 'Hatchback'), ('SUV', 'Sport Utility Vehicle'), ('Sedan', 'Sedan'), ('Sports Car', 'Sports Car')], max_length=64, null=True),
        ),
    ]
