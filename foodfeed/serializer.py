from rest_framework import serializers
from . import models


class AnimalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.animals
        fields = "__all__"


class AnimalitemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.animal_items
        fields = "__all__"


class AnimalitemtypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.animal_item_types
        fields = "__all__"


class AnimalFoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.animal_foods
        fields = "__all__"