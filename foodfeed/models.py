from django.db import models


class animals(models.Model):
    image_1 = models.ImageField(null=True, upload_to="images/")
    image_2 = models.ImageField(null=True, upload_to="images/")
    animal_name = models.CharField(null=True, max_length=20)

    class Meta:
        verbose_name_plural = "animals"

    def __str__(self):
        return f"{self.animal_name}s"




class animal_items(models.Model):
    connected_to_animal = models.ForeignKey(animals, on_delete=models.CASCADE, null=True)
    item_name = models.CharField(null=True, max_length=20)

    class Meta:
        verbose_name_plural = "animal items"

    def __str__(self):
        return f"{self.connected_to_animal} |{self.item_name}"


class animal_item_types(models.Model):
    connected_to_animal_items = models.ForeignKey(animal_items, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, upload_to="animal_item_types/")
    type_name = models.CharField(null=True, max_length=20)

    class Meta:
        verbose_name_plural = "animal item types"

    def __str__(self):
        return f"{self.connected_to_animal_items}   |{self.type_name}"


class animal_foods(models.Model):
    connected_to_animal_items_types = models.ForeignKey(animal_item_types, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, upload_to="animal_foods/")
    food_name = models.CharField(null=True, max_length=40)
    food_price = models.CharField(null=True, max_length=20)
    food_description = models.TextField(null=True, max_length=700)

    class Meta:
        verbose_name_plural = "animal foods"

    def __str__(self):
        return f"{self.connected_to_animal_items_types} |{self.food_name}"