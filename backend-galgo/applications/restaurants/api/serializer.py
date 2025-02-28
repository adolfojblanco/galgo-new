from rest_framework import serializers
from applications.restaurants.models import Restaurant, RestaurantCategory, RestaurantAddress


class RestaurantSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Restaurant
        exclude = ('state', 'deleted_at', 'modified_at', 'create_at')


class RestaurantCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantCategory
        exclude = ('state', 'deleted_at', 'modified_at', 'create_at')


class RestaurantAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantAddress
        exclude = ('state',)