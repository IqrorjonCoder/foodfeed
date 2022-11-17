from django.shortcuts import render


def main(request):
    return render(request, 'main.html')


def animal_name(request, animal_name):
    return render(request, "animal.html", context={"name": animal_name})


def animal_item(request, animal_name, animal_item):
    return render(request, "animal_items.html", context={"name": animal_name,
                                                         "animal_items": animal_item})
