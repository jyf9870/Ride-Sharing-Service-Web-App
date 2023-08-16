# Generated by Django 4.1.5 on 2023-02-06 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride_sharing_service', '0029_merge_20230205_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='requested_vehicle_type',
            field=models.CharField(blank=True, choices=[('SUV', 'Sport Utility Vehicle'), ('Convertible', 'Convertible'), ('Minivan', 'Minivan'), ('Sports Car', 'Sports Car'), ('Truck', 'Pickup Truck'), ('Coupe', 'Coupe'), ('Sedan', 'Sedan'), ('Crossover', 'Crossover'), ('Hatchback', 'Hatchback')], default='', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Confirmed', 'Confirmed'), ('Completed', 'Completed')], default='Open', max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='vehicle_type',
            field=models.CharField(blank=True, choices=[('SUV', 'Sport Utility Vehicle'), ('Convertible', 'Convertible'), ('Minivan', 'Minivan'), ('Sports Car', 'Sports Car'), ('Truck', 'Pickup Truck'), ('Coupe', 'Coupe'), ('Sedan', 'Sedan'), ('Crossover', 'Crossover'), ('Hatchback', 'Hatchback')], max_length=64, null=True),
        ),
    ]
