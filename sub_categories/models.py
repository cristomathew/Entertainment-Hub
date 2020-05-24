from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail
from categories.models import Category
from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor
# Create your models here.
class SubCategory(models.Model):
    title = models.CharField(max_length=200)
    image = fields.ImageField(upload_to='subcategory',blank=True, dependencies=[
        FileDependency(attname='avatar_jpeg', processor=ImageProcessor(
            format='JPEG', scale={'max_width': 500, 'max_height': 600})),
    ])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    seasons = models.IntegerField(default=1)
    def __str__(self):
        return self.title