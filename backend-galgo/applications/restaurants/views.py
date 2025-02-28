from django.shortcuts import render
from rest_framework import generics

from applications.base.api import GeneralListApiView
from applications.restaurants.api.serializer import RestaurantSerializer, RestaurantCategorySerializer, RestaurantAddressSerializer


# Create your views here.

class RestaurantCategoryList(GeneralListApiView):
    serializer_class = RestaurantCategorySerializer


class RestaurantListApiView(GeneralListApiView):
    serializer_class = RestaurantSerializer