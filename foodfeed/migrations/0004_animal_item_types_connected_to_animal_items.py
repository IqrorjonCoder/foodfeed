# Generated by Django 4.0.5 on 2022-11-18 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodfeed', '0003_animal_items_connected_to_animal'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal_item_types',
            name='connected_to_animal_items',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodfeed.animal_items'),
        ),
    ]
