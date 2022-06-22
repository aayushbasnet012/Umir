from logging import raiseExceptions
from random import randint
from rest_framework.response import Response

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import RetrieveModelMixin
from django_filters.rest_framework import DjangoFilterBackend
from food.models import MenuCategory, MenuItems, Table
from food.serializers import MenuCategorySerializer, MenuItemSerializer, TableSerializers
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
# Create your views here.

class MenuCategoryViewSet(ModelViewSet):
    queryset = MenuCategory.objects.all().select_related()
    serializer_class = MenuCategorySerializer
    
    # @method_decorator(cache_page(43200))
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())

    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)



class MenuItemsViewSet(ModelViewSet):
    queryset = MenuItems.objects.all().select_related()
    serializer_class = MenuItemSerializer


def lobby(request):
    return render(request, 'food/lobby.html')

class TableViewSet(ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializers

    filter_backends= [DjangoFilterBackend]
    filterset_fields= ['table_number']

    def list(self, request):
        queryset = Table.objects.all()

        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        serializer.is_valid
        if serializer.data[0]["is_occupied"]==True:
            return Response(serializer.data)
        elif serializer.data[0]["is_occupied"] == False:
            serializer.data[0]["user_id"] = "random user"
            serializer.data
            return Response(serializer.data)
            
