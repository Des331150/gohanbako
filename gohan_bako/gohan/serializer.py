from rest_framework import serializers
from .models import Recipes, Labels

class LabelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labels
        fields = ["id", "name"]

class RecipesSerializer(serializers.ModelSerializer):
    labels = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Recipes
        fields = ["recipe_name", "description", "image", "publication_date", "author", "labels"]

