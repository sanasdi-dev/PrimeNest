from django.urls import path
from . import views

app_name = "property"

urlpatterns = [

    path(
        "",
        views.property_list,
        name="list"
    ),

    path(
        "favorites/",
        views.favorites,
        name="favorites"
    ),

    path(
        "favorite/<int:id>/",
        views.add_to_favorites,
        name="add_favorite"
    ),

    path(
        "<slug:slug>/",
        views.property_detail,
        name="detail"
    ),

]