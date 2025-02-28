from django.urls import path
from applications.restaurants.views import RestaurantCategoryList, RestaurantListApiView

urlpatterns = [
    path('', RestaurantListApiView.as_view(), name='restaurants'),
    path('categories/', RestaurantCategoryList.as_view(), name = 'restaurant_categories')

]