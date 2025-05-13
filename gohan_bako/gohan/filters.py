import django_filters 
from .models import Recipes

class RecipesFilter(django_filters.Filterset):
    class Meta:
        model = Recipes
        fields = ["recipe_name", "description", "author", "publication_date", "labels"]