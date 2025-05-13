from django.shortcuts import redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import User, Recipes
from .serializer import RecipesSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny 
from rest_framework.pagination import PageNumberPagination
# Create your views here.

@api_view(["POST"])
@permission_classes([AllowAny])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def list_recipes(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    recipes = Recipes.objects.all()
    result_page = paginator.paginate_queryset(recipes, request)
    serializer = RecipesSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(["GET"])
def retrieve_recipe(request, id):
    try:
        recipe = Recipes.objects.get(pk=id)
    except Recipes.DoesNotExist:
        return Response({"detail": "Recipe not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = RecipesSerializer(recipe)
    return Response(serializer.data)
    
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_recipe(request):
    if request.method == "POST":
        serializer = RecipesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
