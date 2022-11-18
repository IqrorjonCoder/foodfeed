# Generated by Django 4.0.5 on 2022-11-18 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodfeed', '0004_animal_item_types_connected_to_animal_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='animal_foods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='animal_foods/')),
                ('food_name', models.CharField(max_length=40, null=True)),
                ('food_price', models.CharField(max_length=20, null=True)),
                ('food_description', models.TextField(max_length=700, null=True)),
                ('connected_to_animal_items_types', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='foodfeed.animal_item_types')),
            ],
            options={
                'verbose_name_plural': 'animal foods',
            },
        ),
    ]
