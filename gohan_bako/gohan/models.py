from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Labels(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Recipes(models.Model):
    recipe_name = models.CharField(max_length=240)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="recipes/")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    publication_date = models.DateTimeField(auto_now_add=True)
    labels = models.ManyToManyField(Labels, related_name="recipes")

    def __str__(self):
        return self.recipe_name

