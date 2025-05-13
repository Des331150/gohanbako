import django_filters 
from .models import Recipes, Labels

class RecipesFilter(django_filters.FilterSet):
    labels = django_filters.ModelMultipleChoiceFilter(field_name="labels", queryset=Labels.objects.all())

    order = django_filters.OrderingFilter(
        fields= (("recipe_name", "recipe_name"), ("description", "description"), ("author", "author"), ("publication_date", "publication_date"), ("labels", "labels"))
    )

    class Meta:
        model = Recipes
        fields = ["recipe_name", "description", "author", "publication_date"]
