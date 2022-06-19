from urllib import request
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from food.models import MenuCategory, MenuItems
from food.serializers import MenuCategorySerializer, MenuItemSerializer
# Create your views here.


class MenuCategoryViewSet(ModelViewSet):
    queryset = MenuCategory.objects.all().select_related()
    serializer_class = MenuCategorySerializer

class MenuItemsViewSet(ModelViewSet):
    queryset = MenuItems.objects.all().select_related()
    serializer_class = MenuItemSerializer



def lobby(request):
    return render(request, 'food/lobby.html')
