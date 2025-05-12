from rest_framework import serializers
from .models import Recipes, Labels, User

class LabelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Labels
        fields = ["id", "name"]

class RecipesSerializer(serializers.ModelSerializer):
    labels = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Recipes
        fields = ["recipe_name", "description", "image", "publication_date", "author", "labels"]

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style=({"input_type": "password"}), write_only=True)

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Password fields don't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        user = User.objects.create_user(username=validated_data["username"], email=validated_data["email"], password=validated_data["password"])
        
        return user
    
    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "password2"]
    

