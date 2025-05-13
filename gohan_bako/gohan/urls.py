from django.urls import path
from rest_framework.authtoken import views
from . import views

urlpatterns = [
    path("api/token-auth", views.obtain_auth_token),
    path("gohan/create/",views.create_user, name="create_user"),
    path("gohan/", views.list_recipes, name="list_recipes"),
    path("gohan/<int:id>/", views.retrieve_recipe, name="retrieve_recipe"),
    path("gohan/recipe/create/", views.create_recipe, name="create_recipe")
]