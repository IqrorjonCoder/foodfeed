from django.contrib import admin
from . import models


admin.site.register(models.animals)
admin.site.register(models.animal_items)
admin.site.register(models.animal_item_types)
admin.site.register(models.animal_foods)

