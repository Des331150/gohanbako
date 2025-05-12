from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO
import os

# Create your models here.
class Labels(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Recipes(models.Model):
    recipe_name = models.CharField(max_length=240)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="recipes/", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    publication_date = models.DateTimeField(auto_now_add=True)
    labels = models.ManyToManyField(Labels, related_name="recipes")

    def __str__(self):
        return self.recipe_name
    
    def save(self, *args, **kwargs):
        if self.image:
            try:
                img = Image.open(self.image)
                img.verify()
                
                img =  Image.open(self.image)

                if img.mode in ("RGBA", "LA", "P"):
                    img = img.convert("RGB")

                new_width = 800
                original_width, original_height = img.size
                new_height = int((new_width / original_width) * original_height)

                img = img.resize((new_width, new_height), Image.LANCZOS)   

                temp_img = BytesIO()
                img.save(temp_img, format="JPEG", quality=70, optimize=True)
                temp_img.seek(0)

                original_name, _ = os.path.splitext(self.image.name)
                img = f"{original_name}.jpg"

                self.image.save(img, ContentFile(temp_img.read()), save=False)
            except (IOError, OSError) as e:
                raise ValueError(f"This upload file is not a valid image. -- {e}")
        super().save(*args, **kwargs)



