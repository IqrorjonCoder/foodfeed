# Generated by Django 4.0.5 on 2022-11-18 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodfeed', '0002_animal_item_types_animal_items_alter_animals_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal_items',
            name='connected_to_animal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodfeed.animals'),
        ),
    ]