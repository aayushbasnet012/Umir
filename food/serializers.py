from email.policy import default
from food.models import MenuCategory, MenuItems, Table
from rest_framework import serializers

#create a different serializer for put request
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItems
        fields = ['id','item_name','item_price','item_image', 'item_category','old_price','quantity_type']

class MenuCategorySerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True, read_only=True)
    class Meta:
        model = MenuCategory
        fields = ['id','category_name', 'category_image','items']

class TableSerializers(serializers.ModelSerializer):
    GUID = serializers.UUIDField(read_only=True)
    class Meta:
        model = Table
        fields = ['GUID','table_number','is_occupied']