from django.shortcuts import render
from django.http import HttpResponse
from . import models


def main(request):
    data = {"data": models.animals.objects.all().values('image_1', 'animal_name')}
    return render(request, 'main.html', context=data)

def card(request):
    return render(request, "card.html")


def animal_name(request, animal_name):
    return render(request, "animal.html", context={"name": animal_name})


def animal_item(request, animal_name, animal_item):
    return render(request, "animal_items.html", context={"name": animal_name,
                                                         "animal_items": animal_item})


def food_type(request, animal_name, animal_item, item_type):
    return render(request, "animal_type.html", context={"name": animal_name,
                                                         "animal_items": animal_item,
                                                         "item_type": item_type})


def food(request, animal_name, animal_item, item_type, food_name):
    return render(request, "food.html", context={"name": animal_name,
                                                         "animal_items": animal_item,
                                                         "item_type": item_type,
                                                        "food_name": food_name})
