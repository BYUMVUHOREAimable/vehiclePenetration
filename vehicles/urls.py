from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path("", views.index, name="index"),
    path("vehicles/", views.vehicle_list, name="vehicle_list"),
    path("create/", views.create_vehicle, name="create_vehicle"),
    path("update/<pk>/", views.update_vehicle, name="update_vehicle"),
    path("delete/<pk>/", views.delete_vehicle, name="delete_vehicle"),
]
