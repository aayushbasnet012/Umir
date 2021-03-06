from uuid import UUID, uuid4
from django.db import models


# Create your models here.


class MenuCategory(models.Model):
    category_name = models.CharField(max_length=255, unique=True, default=None)
    category_image = models.ImageField()


class Table(models.Model):
    GUID = models.UUIDField(primary_key=True, default=uuid4)
    table_number = models.CharField(max_length=2)
    is_occupied = models.BooleanField(default=0, blank=False)

    # def __id__(self):
    #     return self.GUID


class MenuItems(models.Model):
    mesurment_per_cup = 'Cup'
    mesurment_per_plate = 'Plate'
    mesurment_per_piece = 'Piece'
    mesurment_per_glass = "Glass"

    mesurment_unit = [
        (mesurment_per_cup, 'Cup'),
        (mesurment_per_plate, 'Plate'),
        (mesurment_per_piece, 'Piece'),
        (mesurment_per_glass, "Glass"),
    ]

    item_name = models.CharField(
        max_length=255, blank=False, default="Not Posted")
    item_price = models.SmallIntegerField()
    item_image = models.ImageField(upload_to="food")
    item_category = models.ForeignKey(
        MenuCategory, on_delete=models.SET_NULL, default=models.SET_NULL, related_name="items", null=True)
    old_price = models.SmallIntegerField()
    quantity_type = models.CharField(
        max_length=255, choices=mesurment_unit, default="Plate")

    def __srt__ (self):
        return self.id

class Orders(models.Model):
    stage_ordered = 'Ordered'
    state_cooking = 'Cooking'
    state_dispatched = 'Dispatched'

    state = [
        (stage_ordered, 'Ordered'),
        (state_dispatched, 'Cooking'),
        (state_cooking, 'Dispatched'),
    ]
    table_id = models.ForeignKey(
        Table, on_delete=models.CASCADE, default=models.SET_NULL, blank=False, null=True)
    item_id = models.ForeignKey(
        MenuItems, on_delete=models.CASCADE, default=models.SET_NULL, blank=False, null=True)
    quantity = models.SmallIntegerField(default=1, blank=False)
    order_state = models.CharField(
        max_length=15, choices=state, blank=False, default="ordered"
    )
