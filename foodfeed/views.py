from django.shortcuts import render
from . import models
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializer



@api_view(['GET'])
def api(request):

    return Response({
        "animals": serializer.AnimalsSerializer(models.animals.objects.all(), many=True).data,
        "animal_items": serializer.AnimalitemsSerializer(models.animal_items.objects.all(), many=True).data,
        "animal_item_types": serializer.AnimalitemtypesSerializer(models.animal_item_types.objects.all(), many=True).data,
        "animal_foods": serializer.AnimalFoodsSerializer(models.animal_foods.objects.all(), many=True).data,
    })







def main(request):
    data = {
        "data": models.animals.objects.all().values('image_1', 'animal_name'),
        "top_ten": models.animal_foods.objects.all().values(),
    }
    return render(request, 'main.html', context=data)


def card(request):
    data = {
        "animal_foods" : models.animal_foods.objects.all().values(),
    }

    return render(request, "card.html", context=data)



def animal_name(request, animal_name):
    data = {
        "image_2": models.animals.objects.filter(animal_name=f"{animal_name}").all().values('image_2'),
        "animal_items": models.animal_items.objects.filter(connected_to_animal=models.animals.objects.filter(animal_name=f"{animal_name}").all().values('id')[0]['id']).all().values(),
        "food_types": models.animal_item_types.objects.all().values(),
    }
    return render(request, "animal.html", context=data)


def animal_item(request, animal_name, animal_item):
    animals_items = models.animal_items.objects.filter(item_name=f"{animal_item}", connected_to_animal_id=models.animals.objects.filter(animal_name=f"{animal_name}").all().values()[0]['id']).all().values()
    data = {
        "image": models.animals.objects.filter(animal_name=f"{animal_name}").all().values()[0],
        "animals": models.animals.objects.filter(animal_name=f"{animal_name}").all().values(),
        "animals_items": animals_items,
        "animals_item_type": models.animal_item_types.objects.filter(connected_to_animal_items_id=animals_items[0]['id']).all().values('id')[0]['id'],
        "animal_foods" : models.animal_foods.objects.filter(connected_to_animal_items_types_id=models.animal_item_types.objects.filter(connected_to_animal_items_id=animals_items[0]['id']).all().values('id')[0]['id']).all().values(),
    }


    return render(request, "animal_items.html", context=data)


def food_type(request, animal_name, animal_item, item_type):
    data = {
        "animal_item_type": models.animal_item_types.objects.filter(connected_to_animal_items_id=models.animal_items.objects.filter(item_name=f"{animal_item}", connected_to_animal_id=models.animals.objects.filter(animal_name=f"{animal_name}").all().values('id')[0]['id']).all().values('id')[0]['id'], type_name=f"{item_type}").all().values()[0],
        "foods": models.animal_foods.objects.filter(connected_to_animal_items_types_id=models.animal_item_types.objects.filter(connected_to_animal_items_id=models.animal_items.objects.filter(item_name=f"{animal_item}", connected_to_animal_id=models.animals.objects.filter(animal_name=f"{animal_name}").all().values('id')[0]['id']).all().values('id')[0]['id'], type_name=f"{item_type}").all().values()[0]['id']).all().values(),
    }
    return render(request, "animal_type.html", context=data)


def food(request, animal_name, animal_item, item_type, food_name):
    data = {"the_food": models.animal_foods.objects.filter(
                food_name=f"{food_name}",
                connected_to_animal_items_types_id=models.animal_item_types.objects.filter(type_name=f"{item_type}",connected_to_animal_items_id=models.animal_items.objects.filter(item_name=f"{animal_item}",connected_to_animal_id=models.animals.objects.filter(animal_name=f"{animal_name}").all().values()[0]['id']).all().values()[0]['id']).all().values()[0]['id']
            ).all().values()[0],
            "likee": models.animal_foods.objects.all().values(),
    }

    return render(request, "food.html", context=data)
